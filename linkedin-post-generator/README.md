# LinkedIn Post Generator - Automated Content from Your Work Sessions

## Overview

**LinkedIn Post Generator** is a Claude Code skill that automatically converts your work sessions into polished, engagement-optimized LinkedIn posts. Build in public and maintain consistent content sharing without extra effort.

Instead of manually summarizing what you built, this skill analyzes your session logs, extracts key accomplishments, and generates 1-2 LinkedIn-ready posts with strategic posting recommendations.

## The Problem

Building and shipping projects is only half the job. You also need to:
- ❌ Manually document what you built
- ❌ Distill technical work into audience-friendly narratives
- ❌ Write multiple versions (long-form and short)
- ❌ Maintain consistent posting schedule
- ❌ Make time for content creation alongside building

## The Solution

Automation. Extract intelligence from your existing work sessions and turn them into content.

## How It Works

### Process

1. **Session Analysis** — Reads your latest Claude Code session logs
2. **Topic Identification** — Extracts 2-3 major accomplishments
3. **User Selection** — You pick which topic to post about now
4. **Content Generation** — Creates 2 polished versions:
   - Long-form (250-300 words) — Full narrative with story arc
   - Short-form (80-120 words) — Punchy version for scrollers
5. **Archive Others** — Saves remaining topics to `post_ideas.json` for future posts
6. **Posting Strategy** — Recommends timing, hashtags, sequencing

## Tech Stack

- **Python 3** — Session analysis & JSON processing
- **Claude Code** — Content generation & intelligence
- **JSON** — Post idea archiving
- **Markdown** — Skill definition

## Getting Started

### Prerequisites
- Claude Code with latest version
- Working session logs at `~/.claude/sessions/`

### Installation
No installation needed. The skill is built into Claude Code.

### Usage

**Generate posts from latest session:**
```
/linkedin-post-generator
```

Choose which topic you want to post about (1, 2, or 3). Other topics automatically save for later.

**View all saved post ideas:**
```
/linkedin-post-generator --upcoming
```

Lists all topics from past sessions, ready to generate posts anytime.

**Generate a post from a saved idea:**
```
/linkedin-post-generator --id 2
```

Pick any saved idea by ID and generate fresh posts.

## Files

| File | Purpose |
|------|---------|
| `linkedin-post-generator-skill.md` | Skill definition & usage guide |
| `post_ideas.json` | Archive of saved post ideas from sessions |

## Features

✅ **Automatic topic extraction** — Identifies 2-3 major accomplishments per session  
✅ **Smart content generation** — Two versions (long & short) for different audiences  
✅ **Persistent idea bank** — Saves unused topics for strategic posting  
✅ **Engagement optimization** — Hooks, CTAs, emoji placement for LinkedIn algorithm  
✅ **Posting strategy** — Timing recommendations, hashtags, sequencing advice  
✅ **Zero extra work** — Uses data you already have (your session logs)  

## Output Format

Each generated post includes:

```
[POST VERSION 1 - LONG FORM]
250-300 words with complete narrative arc
- Hook: Problem or insight
- Build: What you shipped, how
- Impact: Why it matters
- CTA: Engagement question
- 3-5 strategic emojis

[POST VERSION 2 - SHORT FORM]
80-120 words, scannable in 10 seconds
- Core insight
- Key outcome
- Engagement hook
- 2-3 emojis

[POSTING STRATEGY]
- Best time to post
- Suggested hashtags
- Sequencing advice (if part of a series)
```

## Use Cases

- **Build in public** — Document your shipping journey while building
- **Thought leadership** — Share learnings from each project
- **Portfolio building** — Turn work into social proof
- **Consistent posting** — Maintain LinkedIn presence without friction
- **Personal brand** — Build audience as you build products

## Content Bank Example

```json
{
  "last_updated": "2026-05-02T14:36:59",
  "ideas": [
    {
      "id": 1,
      "topic": "Signal Dashboard - Trend Aggregation System",
      "description": "Built real-time trend detector...",
      "session_date": "2026-05-02",
      "suggested_post_date": "2026-05-05"
    },
    {
      "id": 2,
      "topic": "Pinecone Memory Integration",
      "description": "Persistent semantic memory for AI...",
      "session_date": "2026-05-02",
      "suggested_post_date": "2026-05-07"
    }
  ]
}
```

## Strategic Tips

1. **Stagger posts** — Wait 24-48 hours between posts to maximize engagement on each
2. **Series building** — Sequence related projects (shipped → how it works → learnings)
3. **Audience slicing** — Different posts resonate with different audiences
4. **Best times** — Post weekday mornings (8-9am) when builders are active
5. **Hashtag strategy** — Use mix of broad (#BuildInPublic) and specific (#AI, #Automation)

## Example Posts Generated

**Long-form example:**
```
Built persistent semantic memory for Claude Code using Pinecone.

Every conversation used to start from zero. No memory of past 
decisions, preferences, or what worked before...

[continues with narrative]

What would it mean if your AI collaborator actually remembered 
what you've taught it?

#Claude #AI #Development #BuildInPublic
```

**Short-form example:**
```
Built persistent memory for Claude Code. Now Claude remembers...

🧠 Cross-session context (no more cold starts)
⚡ `/recall <topic>` for instant past context
📚 Learns your patterns and preferences

What problems would persistent AI memory solve for you?

#Claude #AI
```

## Future Enhancements

- [ ] Direct LinkedIn API posting (auto-post with approval)
- [ ] Image/screenshot suggestions for each post
- [ ] Analytics integration (track post performance)
- [ ] Multi-platform output (Twitter, Dev.to, Medium)
- [ ] A/B testing of CTA variations
- [ ] Hashtag trending integration

## Analytics

Track performance of generated posts:
- Views, comments, shares on LinkedIn
- Which topics resonate most
- Best posting times for your audience
- Iterate on content themes

## Author

Built as a Claude Code skill for content creators who build in public and want to maintain consistent LinkedIn presence without manual effort.
