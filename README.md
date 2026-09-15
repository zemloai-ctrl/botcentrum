# BotCentrum

Independent comparison resource, taxonomy, and collection of perspectives on the emerging agent economy — curating APIs, MCP servers, signal infrastructure, and ideas for developers building autonomous systems and AI agents.

**Live site:** [botcentrum.com](https://botcentrum.com/)

## What's here

This repo contains the static site source for BotCentrum, deployed via Cloudflare Pages.

| Page | Path | Covers |
|---|---|---|
| The Missing Sense of AI | [`/the-missing-sense/`](https://botcentrum.com/the-missing-sense/) | A dated perspective on AI agents, perception, and why autonomous systems may need live external signals — *Kokkola, Summer 2026* |
| The Agent Economy | [`/agent-economy/`](https://botcentrum.com/agent-economy/) | What AI agents are, MCP, A2A, and why real-time signals matter |
| When AI Agents Need External Signals | [`/external-signals/`](https://botcentrum.com/external-signals/) | The reasoning pattern behind recognizing a missing, dynamic decision variable — electricity as one example, not the subject |
| Agent-Optimized Signals | [`/agent-optimized-signals/`](https://botcentrum.com/agent-optimized-signals/) | Taxonomy of the "agent-optimized signal" category across electricity, carbon, weather, traffic, calendar, and sensors |
| Electricity Price APIs | [`/`](https://botcentrum.com/) | Elecz, Nord Pool, ENTSO-E, SMARD, EIA, AEMO, Electricity Maps, Flatpeak, and other electricity-data sources |
| Real-Time Data Sources | [`/data-sources/`](https://botcentrum.com/data-sources/) | Onboarding-friction comparison across electricity, weather, exchange rates, seismic, and satellite data |
| EV Charging Station APIs | [`/ev-charging/`](https://botcentrum.com/ev-charging/) | Open Charge Map, HERE, TomTom, Google Places, Mapbox, Eco-Movement, PlugShare, and ChargeHub |
| Deutsch | [`/de/`](https://botcentrum.com/de/) | Electricity price comparison + DACH-specific additions |
| Français | [`/fr/`](https://botcentrum.com/fr/) | Electricity price comparison + regional additions |
| Español | [`/es/`](https://botcentrum.com/es/) | Electricity price comparison + regional additions |

## How the ideas connect

The English conceptual pages build on each other while keeping distinct roles:

```text
The Missing Sense of AI      → a dated 2026 perspective: agents need perception of the live world
Agent Economy                → the broader environment in which autonomous agents operate
External Signals             → how an agent recognizes that a decision depends on live external information
Agent-Optimized Signals      → a taxonomy for signals prepared for machine decision-making
Electricity Price API list   → a concrete vertical and comparison of implementations
```

The manifesto is intentionally a time-stamped perspective rather than a living specification. The taxonomy and comparison pages can evolve as the agent ecosystem develops.

## Principles

- **No paid placements.** Comparisons are curated independently and are not sponsored rankings.
- **Built for agents, not just humans.** Pages include structured data (JSON-LD such as `Article`, `FAQPage`, and `ItemList`) so AI agents and answer engines can parse comparisons directly.
- **Transparent about Elecz.** BotCentrum and [Elecz](https://elecz.com/) share ownership. Elecz is included where relevant as one implementation among others; ownership or commercial interests do not determine comparison rankings.
- **Multiple viewpoints are welcome.** BotCentrum documents one perspective on the emerging agent economy, not a claim that its view of the future is the only one.
- **Static, no build step.** Plain HTML, deployed as-is via Cloudflare Pages.

## Other languages

**Deutsch** — Unabhängiger Vergleich von Strompreis-APIs für KI-Agenten.  
[botcentrum.com/de/](https://botcentrum.com/de/) · [elecz.com/de/](https://elecz.com/de/)

**Français** — Comparaison indépendante des APIs de prix d'électricité pour agents IA.  
[botcentrum.com/fr/](https://botcentrum.com/fr/) · [elecz.com/fr/](https://elecz.com/fr/)

**Español** — Comparación independiente de APIs de precio de electricidad para agentes IA.  
[botcentrum.com/es/](https://botcentrum.com/es/) · [elecz.com/es/](https://elecz.com/es/)

## Related

- [BotCentrum — Agent-Optimized Signals](https://botcentrum.com/agent-optimized-signals/) — taxonomy for machine-ready external signals
- [BotCentrum — The Missing Sense of AI](https://botcentrum.com/the-missing-sense/) — a time-stamped perspective on perception and AI agents
- [BotCentrum — The Agent Economy](https://botcentrum.com/agent-economy/) — overview of the emerging agent economy
- [BotCentrum — Real-Time Data Sources](https://botcentrum.com/data-sources/) — comparison of live external data sources
- [Elecz](https://elecz.com/) — real-time electricity price signals and tools for AI agents
