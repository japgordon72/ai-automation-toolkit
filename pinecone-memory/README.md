# Pinecone Memory - Persistent Semantic Context for Claude Code

## Overview

**Pinecone Memory** is a persistent semantic memory system that enables Claude Code to remember past context, decisions, and preferences across sessions. Instead of starting fresh every conversation, Claude learns your working patterns and maintains project continuity.

This is the difference between collaborating with an AI that has institutional memory vs. one that restarts cold every session.

## The Problem

Every Claude Code session traditionally started from zero:
- ❌ No memory of past architectural decisions
- ❌ No context about what worked before
- ❌ No learning of your preferences or code style
- ❌ Multi-week projects lose momentum between sessions
- ❌ Repeating context setup every conversation

## The Solution

Integrate Pinecone semantic memory to give Claude persistent context:
- ✅ Remembers past decisions and their rationale
- ✅ Learns your working preferences and code patterns
- ✅ Uses `/recall <topic>` to instantly surface relevant past conversations
- ✅ Maintains project continuity across time
- ✅ Automatic session logging and embedding

## How It Works

### Architecture

1. **Session Capture** — Each Claude Code session is automatically logged
2. **Embedding** — Session content is embedded using a semantic encoder
3. **Storage** — Embeddings are stored in Pinecone `personal-memory` index
4. **Retrieval** — Use `/recall <topic>` to search by semantic meaning (not keyword matching)
5. **Context** — Retrieved context is surfaced to Claude for decision-making

### Workflow

```
Session Happens
      ↓
Auto-logged to ~/.claude/sessions/
      ↓
upsert_session.py embeds content
      ↓
Stored in Pinecone index
      ↓
User runs: /recall "architecture decisions"
      ↓
pinecone_memory.py retrieves relevant sessions
      ↓
Claude uses context for next steps
```

## Tech Stack

- **Pinecone** — Vector database for semantic search
- **Python 3** — Embedding & query logic
- **Sentence Transformers** — Semantic embeddings
- **Claude Code** — Integration point
- **JSON** — Configuration & session metadata

## Getting Started

### Prerequisites
- Pinecone account (free tier available at https://www.pinecone.io)
- Python 3.8+
- `sentence-transformers` library

### Installation

1. **Get Pinecone API Key:**
   - Sign up at https://www.pinecone.io (free tier)
   - Create index: `personal-memory` (dimension: 384)
   - Copy API key

2. **Install dependencies:**
   ```bash
   pip install sentence-transformers pinecone-client
   ```

3. **Configure API key:**
   ```bash
   # Add to ~/.claude/settings.local.json
   {
     "PINECONE_API_KEY": "your-key-here",
     "PINECONE_INDEX": "personal-memory"
   }
   ```

### Usage

**Upsert current session to memory:**
```bash
python upsert_session.py 2026-05-02.md
```

**Recall past context by topic:**
```bash
/recall "authentication system design"
```

This returns the top 5 most relevant past sessions with similarity scores.

## Files

| File | Purpose |
|------|---------|
| `pinecone_memory.py` | Main `/recall` query script |
| `upsert_session.py` | Embeds & stores session to Pinecone |
| `memory-config.json` | Configuration (index name, dimensions) |
| `recall-skill.md` | Claude Code skill definition |

## Configuration

`memory-config.json`:
```json
{
  "pinecone_index": "personal-memory",
  "embedding_model": "all-MiniLM-L6-v2",
  "embedding_dimension": 384,
  "top_k_results": 5,
  "similarity_threshold": 0.65
}
```

## Features

✅ **Semantic search** — Finds what matters, not just keyword matches  
✅ **Free tier** — Pinecone free tier supports personal memory systems  
✅ **Auto-logging** — Sessions automatically captured, no setup needed  
✅ **Fast retrieval** — Similarity search completes in <500ms  
✅ **Privacy** — Entire system runs locally/in your own Pinecone project  
✅ **Extensible** — Easy to add custom embedding models or storage backends  

## Use Cases

- **Long-running projects** — Maintain context over weeks/months
- **Design decisions** — Quickly recall why architectural choices were made
- **Pattern learning** — Claude learns your code style and preferences
- **Onboarding** — New team members or sessions can reference past context
- **Knowledge capture** — Turn conversations into searchable institutional memory

## Performance

- **Embedding:** ~2-3 seconds per session (300-500 words)
- **Storage:** ~0.5KB per embedding vector
- **Retrieval:** <500ms for top-5 results
- **Cost:** Free tier supports 100K vectors (~1000 sessions)

## Advanced: Customize Embedding Model

Want better embeddings? Use larger models:

```python
from sentence_transformers import SentenceTransformer

# Default (fast, accurate)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Better accuracy, slower
model = SentenceTransformer('all-mpnet-base-v2')

# Production-grade
model = SentenceTransformer('all-MiniLM-L12-v2')
```

## Security Notes

⚠️ **Never commit `settings.local.json`** — Contains live API key  
✅ Use `.gitignore` to exclude all `.local.json` files  
✅ Rotate API keys periodically  
✅ Don't share Pinecone credentials  

## Troubleshooting

**Q: `/recall` returns low similarity scores?**  
A: Increase `top_k_results` in config, or lower `similarity_threshold`

**Q: Embeddings are slow?**  
A: Use `all-MiniLM-L6-v2` (faster) instead of larger models

**Q: Pinecone keeps rejecting my API key?**  
A: Verify key in `settings.local.json` matches your actual Pinecone API key

## Future Enhancements

- [ ] Multi-index support (separate memories for different projects)
- [ ] Automatic session cleanup (delete old sessions)
- [ ] Memory browser UI to visualize past contexts
- [ ] Cross-project memory sharing
- [ ] Real-time memory updates as you work

## Author

Built as a Claude Code system for persistent AI collaboration across sessions.
