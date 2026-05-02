# AI Automation Knowledge Base — Setup Guide

## What You're Building

```
Single video:   Paste URL → n8n fetches transcript → Google Drive → NotebookLM

Channel scan:   Paste channel/playlist URL + keywords → n8n scans ALL videos →
                filters to relevant ones → deduplicates → saves new transcripts →
                logs to Google Sheet → NotebookLM

Weekly auto:    Every Monday → reads channel list from Google Sheet →
                auto-scans all active channels → emails you a summary
```

---

## Files in This Folder

| File | What it is |
|---|---|
| `youtube-transcript-workflow.json` | Single video — import into n8n |
| `youtube-channel-workflow.json` | Channel/playlist scan — import into n8n |
| `youtube-auto-scan-workflow.json` | Weekly auto-scan orchestrator — import into n8n |
| `transcript-trigger.html` | Open in browser — your control panel |
| `SETUP-GUIDE.md` | This guide |

---

## Step 1 — Set Up n8n

**Option A: n8n Cloud (recommended — no install)**
1. Sign up free at **n8n.io** → "Start for free"
2. You get a cloud instance at `https://your-name.app.n8n.cloud`

**Option B: Already have n8n**
Skip to Step 2.

---

## Step 2 — Get a YouTube Data API Key

Required for channel and playlist scanning.

1. Go to **console.cloud.google.com** → sign in with your Google account
2. Click the project selector (top bar) → **"New Project"** → name it anything → **Create**
3. Use the search bar to find **"YouTube Data API v3"** → click it → **Enable**
4. In the left menu → **Credentials** → **"+ Create Credentials"** → **"API Key"**
5. Copy the key (starts with `AIzaSy...`)

Free quota: 10,000 units/day. Scanning a 200-video channel costs ~5 units.

---

## Step 3 — Create the Google Sheet

This powers dedup, logging, and the weekly auto-scan. Takes 2 minutes.

1. Go to **Google Drive** → **New** → **Google Sheets** → name it `YouTube Knowledge Base Config`
2. **Rename the default tab** to `Channels`
3. **Add a second tab** (click `+`) → name it `Processed`
4. In the **Channels** tab, add these headers in row 1:
   - A1: `Channel URL`
   - B1: `Keywords`
   - C1: `Active`
5. Fill in your first channel (row 2):
   - A2: `https://www.youtube.com/@NickSaraev`
   - B2: `n8n, automation, agency, client, workflow`
   - C2: `TRUE`
6. In the **Processed** tab, add these headers in row 1:
   - A1: `Video ID` | B1: `Title` | C1: `Channel` | D1: `Date Processed` | E1: `Preview` | F1: `File Name`
7. **Copy your Sheet ID** from the URL bar:
   `docs.google.com/spreadsheets/d/`**`[THIS IS YOUR SHEET ID]`**`/edit`

---

## Step 4 — Import the Three Workflows into n8n

For each workflow file:
1. Open n8n → click **Workflows** in the left sidebar
2. Click **Add workflow** → **"..."** menu (top right) → **Import from file**
3. Select the file

| File to import | Nodes |
|---|---|
| `youtube-transcript-workflow.json` | 7 nodes |
| `youtube-channel-workflow.json` | 10 nodes |
| `youtube-auto-scan-workflow.json` | 9 nodes |

---

## Step 5 — Connect Your Google Credentials in n8n

You need three Google credentials — all use the same OAuth flow, just different services.

### Google Drive (for saving transcript files)
1. Open `youtube-channel-workflow.json` → click the **"Save to Google Drive"** node
2. Under Credential → **"Create new credential"** → **"Google Drive OAuth2 API"**
3. Follow the OAuth popup → sign in with your Google account
4. Make sure the `AI-Transcripts` folder exists in your Google Drive (create it manually)

### Google Sheets (for dedup logging)
1. In the same workflow → click the **"Log to Processed Sheet"** node
2. Under Credential → **"Create new credential"** → **"Google Sheets OAuth2 API"**
3. Follow the OAuth popup with the same Google account

### Gmail (for failure alerts — optional but recommended)
1. Open `youtube-auto-scan-workflow.json` → click **"Email: Scan Complete"**
2. Under Credential → **"Create new credential"** → **"Gmail OAuth2 API"**
3. Follow the OAuth popup with the same Google account
4. Repeat for the **"Email: Failure Alert"** node

> All three use the same Google account. n8n treats them as separate credentials by service type, but the OAuth sign-in screen is the same each time.

---

## Step 6 — Configure the Auto-Scan Workflow

1. Open `youtube-auto-scan-workflow.json` in n8n
2. Click the **"Configuration"** node (orange Code node at the start)
3. Fill in the three values in the code:
   ```
   sheetId           → your Google Sheet ID from Step 3
   channelWebhookUrl → copy from youtube-channel-workflow's Webhook node
   apiKey            → your YouTube Data API key from Step 2
   ```
4. Save the workflow

**To change the schedule:** Click the **"Every Monday 9am"** trigger → edit the Cron expression
- Every Monday 9am: `0 9 * * 1`
- Every day at 8am: `0 8 * * *`
- Every Sunday at noon: `0 12 * * 0`

---

## Step 7 — Activate All Three Workflows

For each workflow:
1. Click the **Active** toggle (top right) → set to **On**
2. Click the **Webhook** node to confirm the webhook URL

| Workflow | Webhook path |
|---|---|
| Single video | `/webhook/youtube-transcript` |
| Channel scan | `/webhook/youtube-channel` |
| Auto-scan | No webhook — triggered by schedule |

---

## Step 8 — Set Up the Control Panel

1. Double-click `transcript-trigger.html` to open it in your browser
2. Click the **Settings** tab and fill in:
   - **Single Video Webhook URL** — from `youtube-transcript-workflow`
   - **Channel Webhook URL** — from `youtube-channel-workflow`
   - **YouTube Data API Key** — from Step 2
   - **Google Sheet ID** — from Step 3 (enables dedup + logging)
3. Click **Save** after each field

---

## Step 9 — Set Up NotebookLM

1. Go to **notebooklm.google.com** → **New Notebook** → name it `AI Automation Business Guide`
2. Click **Add Source** → **Google Drive** → navigate to `AI-Transcripts` → select all files
3. **Also add your Google Sheet as a source:**
   - Add Source → **Google Drive** → find `YouTube Knowledge Base Config`
   - This sheet becomes a live index — NotebookLM can answer "which video covers X?"

---

## Step 10 — Run Your First Scan

1. Open `transcript-trigger.html` in your browser
2. Go to the **Channel / Playlist** tab
3. Paste: `https://www.youtube.com/@NickSaraev`
4. Keywords: `n8n, automation, agency, client, workflow`
5. Click **Scan & Save Matching Transcripts**

You'll see a stats panel appear:
- **Scanned** — total videos on the channel
- **Matched** — videos whose title/description contained a keyword
- **Already Saved** — skipped (already in your knowledge base)
- **New** — being saved to Google Drive right now

Check your `AI-Transcripts` folder in a few minutes — files will appear one by one.

---

## Step 11 — Start Querying in NotebookLM

After adding sources, use the chat panel on the right:

**Q&A:**
- "What tools are mentioned most across all videos?"
- "What's the recommended way to find the first client?"
- "What services are easiest to deliver as a solo operator?"
- "What are the most common pricing models mentioned?"

**Action plans:**
- "Give me a 30-day action plan to start an AI automation agency from scratch"
- "Create a step-by-step checklist for closing the first client"
- "Summarize all advice about packaging AI automation services"

---

## Ongoing Usage

| Task | How |
|---|---|
| Add a single video | Single Video tab → paste URL → Enter |
| Scan a channel for new content | Channel tab → paste URL + keywords → Scan |
| Add a new channel to weekly scan | Open Google Sheet → Channels tab → add row with URL, keywords, TRUE |
| Pause a channel from auto-scan | Change column C to FALSE in the Channels sheet |
| View everything saved | Open the Processed tab in your Google Sheet |

---

## Troubleshooting

| Problem | Fix |
|---|---|
| "Channel not found" | Use full URL format: `https://www.youtube.com/@Handle` |
| "No videos matched keywords" | Try shorter single words; check the channel actually has relevant content |
| "All matching videos already saved" | Normal! Nothing new since last scan |
| No transcript content | Video has no English captions — a placeholder file is saved, skip it |
| Google Drive auth fails | Use the same Google account in n8n as the Drive where AI-Transcripts lives |
| Google Sheets 403 error | The Sheets credential needs to be set up separately from Drive (Step 5) |
| Auto-scan doesn't fire | Confirm the workflow is Active; check n8n's Executions tab for errors |
| No Gmail alert | Gmail credential must be added to both email nodes separately |
| Sheet ID not found | Must be the ID string between `/d/` and `/edit` in the Google Sheets URL |
