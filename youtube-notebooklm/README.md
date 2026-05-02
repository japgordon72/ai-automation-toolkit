# YouTube-to-NotebookLM Automation - Turn Videos into AI-Generated Study Guides

## Overview

**YouTube-to-NotebookLM** is an end-to-end automation system that transforms YouTube videos into structured study guides, summaries, and interactive learning materials using Google NotebookLM.

Build a personal knowledge base from any YouTube content—educational channels, conference talks, tutorials—without manual transcription or summarization.

## The Problem

YouTube has unlimited knowledge, but extracting it is manual and time-consuming:
- ❌ Watch entire videos (hours)
- ❌ Manual note-taking (error-prone, incomplete)
- ❌ Create study guides (tedious)
- ❌ Convert to searchable knowledge base (lots of work)
- ❌ Scale to multiple videos (not feasible)

## The Solution

Automation from video URL → transcript → NotebookLM study guide in minutes.

## How It Works

### Three Automated Workflows

#### 1. YouTube Transcript Workflow
- Accepts single YouTube video URL
- Extracts transcript via YouTube API
- Cleans & formats transcript
- Uploads to Google Drive
- Creates NotebookLM guide
- Returns study guide link

**Use case:** "Turn this lecture into a study guide"

#### 2. YouTube Channel Workflow
- Accepts YouTube channel URL
- Fetches last N videos from channel
- Processes each video in parallel
- Creates NotebookLM guide for each
- Builds organized folder structure
- Returns links to all guides

**Use case:** "Build knowledge base from entire course channel"

#### 3. Auto-Scan Workflow
- Watches specified YouTube channels/playlists
- Automatically processes new uploads
- Creates NotebookLM guides on schedule
- Maintains updated knowledge base
- Sends notifications of new guides

**Use case:** "Keep knowledge base current with latest uploads"

### Architecture

```
YouTube Video(s)
      ↓
Extract Transcript (YouTube API)
      ↓
Clean & Format
      ↓
Upload to Google Drive
      ↓
NotebookLM API
      ↓
Generate Study Guide
      ↓
Interactive Learning Material
```

## Tech Stack

- **n8n** — Workflow automation platform
- **YouTube API** — Video & transcript extraction
- **Google Drive API** — File storage
- **Google NotebookLM API** — Study guide generation
- **JSON** — Workflow definitions
- **HTML** — Custom trigger UI

## Files

| File | Purpose |
|------|---------|
| `youtube-transcript-workflow.json` | Single video → study guide |
| `youtube-channel-workflow.json` | Full channel → organized guides |
| `youtube-auto-scan-workflow.json` | Automatic new video processing |
| `transcript-trigger.html` | Custom web form for triggering workflows |
| `SETUP-GUIDE.md` | Detailed setup & configuration instructions |
| `youtube-kb-skill.md` | Claude Code skill definition |

## Getting Started

### Prerequisites
- n8n instance (cloud or self-hosted)
- Google account (YouTube, Google Drive, Google Cloud)
- NotebookLM access
- YouTube API key
- Google Drive API credentials

### Quick Start

1. **Read SETUP-GUIDE.md** — Detailed step-by-step configuration
2. **Import workflows** — Upload `.json` files to your n8n instance
3. **Configure credentials** — Add YouTube API key, Google credentials
4. **Test** — Use `transcript-trigger.html` to submit test video
5. **Deploy** — Schedule auto-scan or trigger manually

### Configuration

See `SETUP-GUIDE.md` for detailed:
- YouTube API setup
- Google Drive folder structure
- NotebookLM integration
- Trigger configuration
- Automation scheduling

## Features

✅ **Fully automated** — One URL → complete study guide  
✅ **Batch processing** — Process entire channels or playlists  
✅ **Scheduled automation** — Auto-detect and process new uploads  
✅ **Google Drive integration** — Organized folder structure  
✅ **NotebookLM quality** — AI-powered study guides, not basic summaries  
✅ **Custom triggers** — Web form, webhooks, scheduled runs  
✅ **Error handling** — Handles private videos, captions-only, etc.  
✅ **Notifications** — Alerts when new guides are created  

## Use Cases

### Personal Learning
- Build knowledge base from educational YouTube channels
- Create study guides from lecture recordings
- Organize by topic/course

### Professional Development
- Extract insights from industry conference talks
- Create training materials from tutorial videos
- Build searchable video library

### Content Curation
- Monitor creator channels for new content
- Automatically summarize important releases
- Share guides with team/community

### Knowledge Management
- Convert video knowledge to searchable text
- Create quiz questions from transcripts
- Build AI-powered teaching assistants

## Workflow Breakdown

### Workflow 1: Single Video
```
Input: YouTube URL
    ↓
Fetch Video Metadata
    ↓
Extract Transcript
    ↓
Create Google Drive Folder
    ↓
Upload Transcript
    ↓
Call NotebookLM API
    ↓
Generate Study Guide
    ↓
Output: Study guide link
```

### Workflow 2: Channel
```
Input: YouTube Channel URL
    ↓
Fetch Last 10 Videos
    ↓
For Each Video:
  - Extract Transcript
  - Create NotebookLM Guide
  - Save to Drive
    ↓
Output: Organized folder with all guides
```

### Workflow 3: Auto-Scan
```
Scheduled Trigger (Daily/Weekly)
    ↓
Check Subscribed Channels for New Videos
    ↓
For Each New Video:
  - Process Transcript
  - Create Study Guide
  - Move to Auto-Processed Folder
  - Send Notification
    ↓
Loop: Repeat on schedule
```

## Performance

- **Single video processing:** 2-5 minutes (depends on length)
- **Channel batch:** 30+ videos/hour (depends on video length)
- **Study guide generation:** 1-2 minutes via NotebookLM
- **Storage:** ~2MB per guide (transcript + metadata)

## Integration Examples

### Slack Notifications
Add step to post guide link to Slack when new guide created.

### Zapier Forwarding
Send guide links to email, note apps, or task managers.

### Custom Webhooks
Trigger from other automation platforms.

## Limitations & Edge Cases

- **Private videos** — Requires channel access
- **No captions** — Auto-captioning may be lower quality
- **Length limits** — Very long videos (3+ hours) may timeout
- **Rate limiting** — YouTube & Google Drive have API quotas

See SETUP-GUIDE.md for handling edge cases.

## Future Enhancements

- [ ] Multi-language support (auto-translate transcripts)
- [ ] Custom prompt templates for study guides
- [ ] Quiz generation from transcripts
- [ ] Video highlight extraction (key moments)
- [ ] Citation formatting (APA, MLA, etc.)
- [ ] Integration with flashcard apps (Anki)

## Troubleshooting

**Q: "Invalid API key" error?**  
A: Verify YouTube API key in n8n credentials. Check API is enabled in Google Cloud.

**Q: "Quota exceeded" error?**  
A: YouTube/Google Drive have rate limits. Check quotas in Cloud Console, wait for reset.

**Q: NotebookLM guide is blank?**  
A: Video may not have captions or transcript. Check transcript availability.

**Q: Workflow runs but no guide created?**  
A: Check n8n logs for errors. Verify Google Drive & NotebookLM credentials are valid.

See SETUP-GUIDE.md for detailed troubleshooting.

## Author

Built as an n8n automation for converting YouTube knowledge into structured, searchable learning materials.
