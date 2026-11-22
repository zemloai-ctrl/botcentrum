"""Notify IndexNow (Bing, Yandex, Seznam, Naver...) about changed pages after a deploy.

Changed HTML pages in the pushed commits are mapped to their public URLs.
Submits every URL in sitemap.xml when run manually or when the head commit
message contains "[indexnow-all]". Never fails the deploy.
"""
import json, os, re, subprocess, sys, time, urllib.request, urllib.error

HOST = "botcentrum.com"
KEY = "d6e950a50990e50a982d9c07357c4a6c"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"


def sitemap_urls():
    with open("sitemap.xml", encoding="utf-8") as f:
        return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", f.read())


def changed_urls(before, after):
    if not before or set(before) == {"0"}:
        return sitemap_urls()
    try:
        out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AM", before, after],
                             check=True, capture_output=True, text=True).stdout.split()
    except subprocess.CalledProcessError as e:
        print("git diff failed, submitting sitemap:", e.stderr.strip())
        return sitemap_urls()
    urls = []
    for path in out:
        if path == "index.html":
            urls.append(f"https://{HOST}/")
        elif path.endswith("/index.html") and not path.startswith("."):
            urls.append(f"https://{HOST}/{path[:-len('index.html')]}")
    return urls


def key_file_live():
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(KEY_LOCATION, headers={"User-Agent": "botcentrum-indexnow"}), timeout=20) as r:
                if r.read().decode().strip() == KEY:
                    return True
        except Exception as e:  # noqa: BLE001
            print("key file not reachable yet:", e)
        time.sleep(10)
    return False


def main():
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    head_msg = os.environ.get("HEAD_COMMIT_MESSAGE", "")
    if event == "workflow_dispatch" or "[indexnow-all]" in head_msg:
        urls = sitemap_urls()
    else:
        urls = changed_urls(os.environ.get("BEFORE_SHA", ""), os.environ.get("AFTER_SHA", "HEAD"))
    urls = sorted(set(urls))
    if not urls:
        print("No changed pages; nothing to submit.")
        return 0
    if not key_file_live():
        print("Key file not served at", KEY_LOCATION, "- skipping IndexNow.")
        return 0
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": KEY_LOCATION, "urlList": urls}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print("IndexNow response:", r.status, "for", len(urls), "URLs")
    except urllib.error.HTTPError as e:
        print("IndexNow error:", e.code, e.read().decode()[:300])
    for u in urls:
        print(" -", u)
    return 0


if __name__ == "__main__":
    sys.exit(main())
