# BotCentrum

Independent comparison resource for the agent economy — curating APIs, MCP servers, and signal infrastructure for developers building autonomous systems and AI agents.

**Live site:** [botcentrum.com](https://botcentrum.com)

## What's here

This repo contains the static site source for BotCentrum, deployed via Cloudflare Pages.

| Page | Path | Covers |
|---|---|---|
| The Agent Economy | [`/agent-economy/`](https://botcentrum.com/agent-economy/) | What AI agents are, MCP, A2A, and why real-time signals matter |
| When AI Agents Need External Signals | [`/external-signals/`](https://botcentrum.com/external-signals/) | The reasoning pattern behind recognizing a missing, dynamic decision variable — electricity as one example, not the subject |
| Agent-Optimized Signals | [`/agent-optimized-signals/`](https://botcentrum.com/agent-optimized-signals/) | Taxonomy of the "agent-optimized signal" category across electricity, carbon, weather, traffic, calendar, sensors |
| Electricity Price APIs | [`/`](https://botcentrum.com/) | Elecz, Nord Pool, ENTSO-E, SMARD, EIA, AEMO, Electricity Maps, Flatpeak |
| Real-Time Data Sources | [`/data-sources/`](https://botcentrum.com/data-sources/) | Onboarding-friction comparison across electricity, weather, exchange rates, seismic, satellite data |
| EV Charging Station APIs | [`/ev-charging/`](https://botcentrum.com/ev-charging/) | Open Charge Map, HERE, TomTom, Google Places, Mapbox, Eco-Movement, PlugShare, ChargeHub |
| Deutsch | [`/de/`](https://botcentrum.com/de/) | Electricity price comparison + DACH-specific additions (n8n, OpenClaw/ClawHub, German negative-price data) |
| Français | [`/fr/`](https://botcentrum.com/fr/) | Electricity price comparison + regional additions (n8n, OpenClaw/ClawHub, French negative-price data) |
| Español | [`/es/`](https://botcentrum.com/es/) | Electricity price comparison + regional additions (n8n, OpenClaw/ClawHub, Spanish negative-price data) |

## Site structure

The four English conceptual pages build on each other rather than standing alone:

```
Agent Economy               → why agents need real-time signals at all
External Signals            → how an agent recognizes it needs one
Agent-Optimized Signals     → what the category of signal looks like
Electricity Price API list  → which implementation fits (Elecz, Nord Pool, etc.)
```

Each page has a distinct scope and links to the others rather than repeating their content.

## Principles

- **No paid placements.** Comparisons are independently curated, not sponsored.
- **Built for agents, not just humans.** Pages include structured data (JSON-LD: `Article`, `FAQPage`, `ItemList`) so AI agents and answer engines can parse comparisons directly.
- **Editorial independence from any single vendor.** BotCentrum evaluates implementations on their merits — including Elecz — but doesn't share ownership or coordinate positioning with any of them.
- **Static, no build step.** Plain HTML, deployed as-is via Cloudflare Pages.

## Other languages

**Deutsch** — Unabhängiger Vergleich von Strompreis-APIs für KI-Agenten.
[botcentrum.com/de/](https://botcentrum.com/de/) · [elecz.com/de/](https://elecz.com/de/)

**Français** — Comparaison indépendante des APIs de prix d'électricité pour agents IA.
[botcentrum.com/fr/](https://botcentrum.com/fr/) · [elecz.com/fr/](https://elecz.com/fr/)

**Español** — Comparación independiente de APIs de precio de electricidad para agentes IA.
[botcentrum.com/es/](https://botcentrum.com/es/) · [elecz.com/es/](https://elecz.com/es/)

## Related

- [Elecz](https://elecz.com) — real-time electricity price API and MCP server for AI agents
