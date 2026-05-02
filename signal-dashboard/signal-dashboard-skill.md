# Signal Dashboard

Generate a dashboard of trending AI/automation signals from multiple sources, analyze sentiment, detect early adopter activity, and auto-generate content outlines.

## When to Use

- Every morning to stay ahead of trends in AI/automation space
- Before creating content to understand what builders and knowledge seekers are excited about
- To identify signal-from-noise in a noisy tech landscape
- To track sentiment shifts and early adopter momentum

## What It Does

1. **Fetches signals** from Hacker News, ArXiv, GitHub, and Reddit (all free APIs)
2. **Scores relevance** to AI/automation using keyword matching
3. **Detects early adopter activity** using velocity/score metrics
4. **Analyzes sentiment** of community discussion
5. **Ranks signals** by combined relevance + early adopter score
6. **Auto-generates content outlines** for top signals (5 key points each)
7. **Creates an HTML dashboard** you can open and browse
8. **Prints a summary** of top 5 signals to terminal

## Output

- **HTML Dashboard**: `~/.claude/signal_dashboard/output/YYYY-MM-DD.html`
  - Browsable dashboard with top 10 signals
  - Color-coded source badges (Hacker News, ArXiv, GitHub, Reddit)
  - Relevance and early adopter scores for each signal
  - Direct links to original sources

- **Terminal Summary**: Top 5 signals with content outlines printed to console

## How to Use

```
/signal-dashboard
```

That's it. Claude will handle the rest.

## Data Sources

| Source | Frequency | Signal Type | Cost |
|--------|-----------|------------|------|
| Hacker News | Real-time | Builder mindshare, upvotes as signal | Free |
| ArXiv | Daily | Research breakthroughs (cs.AI, cs.LG, cs.RO) | Free |
| GitHub | Real-time | New tools, star velocity | Free |
| Reddit | Real-time | Nuanced sentiment, real user pain points | Free |

## Content Outline Format

For each top signal, Claude generates:

```
**Signal:** [Title]
**Source:** [Where it appeared]
**Sentiment:** Excited / Skeptical / Mixed
**Early Adopter Score:** High / Medium / Low

### Content Outline
1. **Hook:** Why does this matter NOW? What's the immediate relevance for builders?
2. **What's New:** What specifically is novel vs. hype/old news?
3. **Practical:** How can builders use this today? What can they do right now?
4. **Future:** What does this signal mean for the next 6-12 months?
5. **CTA:** What should your audience explore/try/watch next?
```

## Implementation Steps

1. Run signal fetching script (HN, ArXiv, GitHub, Reddit in parallel)
2. Rank signals by relevance + early adopter score
3. Analyze top 5 signals for sentiment and generate content outlines
4. Generate HTML dashboard
5. Print summary to console

---

## Step-by-Step Instructions for Claude

### Step 1: Fetch signals from all sources
Run the fetch script in parallel to collect raw signals:

```bash
python ~/.claude/signal_dashboard/fetch_signals.py > /tmp/signals.json
```

This outputs a JSON file with:
- All fetched signals from HN, ArXiv, GitHub, Reddit
- Relevance scores (0-10)
- Early adopter scores (0-10)
- Original URL, title, source

### Step 2: Read the signals JSON
Read `/tmp/signals.json` to see what signals were fetched.

### Step 3: Analyze top signals and generate content outlines
From the signals JSON, take the top 5 signals (by combined score) and:

1. **Assess sentiment** — Is the community excited, skeptical, or mixed based on upvotes, discussion, context?
2. **Score early adopter activity** — Is this brand new? Are early adopters jumping on it?
3. **Generate content outline** for each using the 5-point format above

Output this analysis as structured JSON for the next step.

### Step 4: Generate the HTML dashboard
Run the dashboard generator with the signals:

```bash
python ~/.claude/signal_dashboard/generate_dashboard.py /tmp/signals.json
```

This creates: `~/.claude/signal_dashboard/output/YYYY-MM-DD.html`

### Step 5: Print summary to terminal
Display the top 5 signals with their content outlines in a readable format:

```
🚀 TODAY'S TOP AI/AUTOMATION SIGNALS

1. [SIGNAL TITLE]
   Source: GitHub | Sentiment: Excited | Early Adopter: High
   
   Content Outline:
   1. Hook: [...]
   2. What's New: [...]
   3. Practical: [...]
   4. Future: [...]
   5. CTA: [...]

   [URL]

2. [SIGNAL TITLE]
   ...
```

### Step 6: Final message
Print a message indicating:
- Total signals fetched
- Dashboard location
- How to open in browser
