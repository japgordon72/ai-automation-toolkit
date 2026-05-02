You are helping manage a YouTube-to-NotebookLM knowledge base system built with n8n, Google Drive, and Google Sheets.

## System context

The knowledge base pipeline:
- `youtube-transcript-workflow.json` — single video → Google Drive
- `youtube-channel-workflow.json` — channel/playlist + keyword filter + dedup → Google Drive + Google Sheets log
- `youtube-auto-scan-workflow.json` — weekly Cron → reads Channels sheet → triggers channel workflow for each active channel
- `transcript-trigger.html` — browser control panel (single video tab, channel tab, settings tab)
- Google Sheet "YouTube Knowledge Base Config": Channels tab (Channel URL | Keywords | Active), Processed tab (Video ID | Title | Channel | Date | Preview | File Name)
- Google Drive folder `AI-Transcripts` — all transcript `.txt` files
- NotebookLM — AI chat over the transcripts + the Google Sheet as a live index

## Request

$ARGUMENTS

## How to respond

- If the request is about adding a channel: provide the exact row to add to the Channels sheet and suggest keywords
- If the request is about changing keywords: explain the tradeoff (broader = more videos, narrower = higher signal)
- If the request is about a workflow error: diagnose based on the node names and suggest a fix
- If the request is about NotebookLM queries: write specific, well-formed prompts for the topic
- If the request is about extending the system: design the change as a minimal addition to the existing workflows, reusing existing nodes and patterns
- Always prefer editing existing files over creating new ones
- Keep suggestions no-code/low-code unless the user asks for code
