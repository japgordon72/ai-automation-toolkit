# AI Automation Toolkit

A collection of four production-ready automation systems built to solve real problems in trend detection, AI memory, content creation, and knowledge management. Each tool is independently deployable and demonstrates end-to-end system thinking — not just gluing APIs together.

**Built by:** Japheth Gordon · [japgordon@gmail.com](mailto:japgordon@gmail.com) · [LinkedIn](https://linkedin.com/in/japgordon) · [GitHub](https://github.com/japgordon72)

---

## Tools

| Tool | What it does | Stack | Key Skill |
|---|---|---|---|
| [Signal Dashboard](#1-signal-dashboard) | Aggregates AI/automation trends from 4 APIs, scores by relevance + momentum, generates interactive dashboard | Python, 4 APIs, HTML/JS | Data aggregation, scoring algorithms |
| [Pinecone Memory](#2-pinecone-memory) | Gives Claude persistent semantic memory across sessions — `/recall <topic>` surfaces relevant past context instantly | Python, Pinecone, Sentence Transformers | Vector search, embeddings, RAG |
| [LinkedIn Post Generator](#3-linkedin-post-generator) | Analyzes work sessions and generates polished LinkedIn posts (long + short) with posting strategy | Python, Claude API | LLM prompt engineering, content automation |
| [YouTube → NotebookLM](#4-youtube--notebooklm) | Transforms YouTube videos, channels, and playlists into structured study guides automatically | n8n, YouTube API, Google Drive API, NotebookLM | Workflow automation, API orchestration |

---

## 1. Signal Dashboard

**Real-time AI/automation trend aggregator with intelligent scoring.**

Replaces manually checking 10+ sources daily. Fetches signals from Hacker News, ArXiv, GitHub, and Reddit in parallel, ranks them by a dual-factor algorithm (60% relevance + 40% early-adopter momentum), and renders an interactive dashboard with content outlines for the top signals.

```
fetch_signals.py → signals.json → generate_dashboard.py → output/dashboard.html
```

**Quick start:**
```bash
cd signal-dashboard
pip install requests
python fetch_signals.py
python generate_dashboard.py signals.json
```

**Impact:** ~50 signals processed in <5 seconds · Replaces 30–45 min of daily manual source-checking

[→ Full docs](./signal-dashboard/README.md)

---

## 2. Pinecone Memory

**Persistent semantic memory system for Claude Code.**

Every AI session starts cold by default — no memory of past decisions, architectural choices, or working patterns. This system captures sessions, embeds them with `all-MiniLM-L6-v2`, stores them in a Pinecone vector index, and surfaces relevant past context on demand via `/recall`.

```
Session log → upsert_session.py → Pinecone index
/recall "auth decisions" → pinecone_memory.py → top-5 relevant sessions
```

**Quick start:**
```bash
cd pinecone-memory
pip install sentence-transformers pinecone-client
python upsert_session.py your-session.md
# Then in Claude Code:
# /recall "topic you want to remember"
```

**Impact:** Cold starts eliminated on multi-week projects · <500ms retrieval · Free Pinecone tier supports ~1,000 sessions

[→ Full docs](./pinecone-memory/README.md)

---

## 3. LinkedIn Post Generator

**Converts work sessions into polished LinkedIn posts automatically.**

Reads Claude Code session logs, extracts 2–3 major accomplishments, generates two versions of each post (250–300 word long-form + 80–120 word short-form), archives unused ideas to a searchable bank, and recommends timing and hashtag strategy.

```
/linkedin-post-generator → session analysis → topic selection → 2 post versions + strategy
```

**Quick start:**
```
# In Claude Code:
/linkedin-post-generator
```

**Impact:** Eliminates manual content summarization · Maintains consistent LinkedIn presence without extra effort · Builds build-in-public momentum

[→ Full docs](./linkedin-post-generator/README.md)

---

## 4. YouTube → NotebookLM

**End-to-end automation: YouTube video → AI study guide.**

Three n8n workflows covering every use case: single video, full channel batch processing, and auto-scan for new uploads. Extracts transcripts via YouTube API, uploads to Google Drive, feeds to NotebookLM, and returns a structured study guide.

```
YouTube URL → transcript extraction → Google Drive upload → NotebookLM → study guide link
```

**Quick start:**
```
1. Import .json workflow files into your n8n instance
2. Configure YouTube API + Google credentials
3. Open transcript-trigger.html and submit a video URL
```

**Impact:** 2–5 min per video · 30+ videos/hour batch mode · Converts unlimited video knowledge to searchable text

[→ Full docs](./youtube-notebooklm/README.md)

---

## Project Structure

```
ai-automation-toolkit/
├── signal-dashboard/
│   ├── fetch_signals.py          # Parallel API fetch + dual-factor scoring
│   ├── generate_dashboard.py     # HTML dashboard generator
│   ├── dashboard_template.html   # Animated UI template
│   └── config.json               # Keywords, subreddits, ArXiv categories
├── pinecone-memory/
│   ├── pinecone_memory.py        # /recall query logic
│   ├── upsert_session.py         # Session embedding + Pinecone upsert
│   └── memory-config.json        # Index config, embedding model, top-k
├── linkedin-post-generator/
│   ├── linkedin-post-generator-skill.md  # Claude Code skill definition
│   └── post_ideas.json           # Persistent content idea bank
└── youtube-notebooklm/
    ├── youtube-transcript-workflow.json  # Single video workflow
    ├── youtube-channel-workflow.json     # Full channel batch workflow
    ├── youtube-auto-scan-workflow.json   # Auto-scan for new uploads
    ├── transcript-trigger.html   # Web form trigger UI
    └── SETUP-GUIDE.md            # Step-by-step configuration
```

---

## Skills Demonstrated

| Skill | Where |
|---|---|
| Python scripting | Signal Dashboard, Pinecone Memory, LinkedIn Post Generator |
| API integration (REST) | HN, ArXiv, GitHub, Reddit, YouTube, Google Drive |
| Vector databases + embeddings | Pinecone Memory (Pinecone + Sentence Transformers) |
| RAG pipeline design | Pinecone Memory — same pattern used in production AI systems |
| Workflow automation (n8n) | YouTube → NotebookLM (3 workflows, webhooks, scheduling) |
| LLM prompt engineering | LinkedIn Post Generator (session analysis + structured output) |
| Scoring algorithm design | Signal Dashboard (dual-factor weighted ranking) |
| HTML/CSS/JS frontend | Signal Dashboard (animated dashboard), transcript-trigger.html |
| System design | All tools: structured input → processing → useful output |
| Documentation | Every tool has full README, setup guide, and usage examples |

---

## Why These Tools Exist

Each tool was built to solve a real bottleneck in an AI-assisted workflow:

- **Signal Dashboard** → Monitoring 10+ sources for trends was eating 30–45 min/day
- **Pinecone Memory** → Multi-week projects lost context between sessions, requiring re-explaining decisions
- **LinkedIn Post Generator** → Shipping work but not sharing it = invisible portfolio
- **YouTube → NotebookLM** → Valuable video content was locked in watch-only format, not searchable

The philosophy: **automate the repetitive, preserve the creative.** Let systems handle signal aggregation, memory management, and content formatting so time stays focused on high-leverage work.

---

## Getting Started

Each tool is self-contained. Install only what you need:

```bash
# Signal Dashboard — no API keys required
cd signal-dashboard && pip install requests && python fetch_signals.py

# Pinecone Memory — requires free Pinecone account
cd pinecone-memory && pip install sentence-transformers pinecone-client

# LinkedIn Post Generator — requires Claude Code
# Install Claude Code, then: /linkedin-post-generator

# YouTube → NotebookLM — requires n8n + Google account
# See youtube-notebooklm/SETUP-GUIDE.md
```

---

## Part of a Larger AI Stack

This toolkit is one layer of a broader AI automation system built across multiple clients and projects:

| Project | Description | Repo |
|---|---|---|
| **Triton Peptide Protocol Tool** | RAG-powered clinical decision support · FastAPI + Next.js + Pinecone | [view](https://github.com/japgordon72/triton-peptide-protocol) |
| **YouTube Playbook Generator** | Python + Claude API · transforms videos into structured playbooks | [view](https://github.com/japgordon72/youtube-playbook-generator) |
| **AI Automation Toolkit** | This repo | — |

---

## Contact

Interested in AI automation, RAG systems, or workflow architecture?

- **Email:** japgordon@gmail.com
- **LinkedIn:** [linkedin.com/in/japgordon](https://linkedin.com/in/japgordon)
- **GitHub:** [github.com/japgordon72](https://github.com/japgordon72)

---

## License

MIT — use, modify, extend freely.
