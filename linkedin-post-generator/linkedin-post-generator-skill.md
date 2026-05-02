# LinkedIn Post Generator

**Description:** Generate focused LinkedIn posts from your Claude Code sessions. Identifies multiple topics, lets you choose one to post now, and saves the rest for future content.

## When to Use

- After finishing a meaningful work session to generate shareable content
- To convert technical accomplishments into engaging LinkedIn narratives
- To maintain consistent content sharing with strategic spacing
- When you want focused posts on single topics (not session summaries)

## What It Does

1. **Reads your latest session** from `~/.claude/sessions/`
2. **Identifies 2-3 major topics/accomplishments** from that session
3. **Shows you the options** so you can pick which to post about now
4. **Generates 1-2 focused posts** just for your chosen topic
5. **Saves unused topics** to `~/.claude/post_ideas.json` for future posts
6. **Outputs formatted posts** ready to copy-paste
7. **Provides posting recommendations** — timing, hashtags, sequencing

## Output Format

```
[AVAILABLE TOPICS]
1. [Topic A] — [Brief description]
2. [Topic B] — [Brief description]
3. [Topic C] — [Brief description]

Choose which topic to generate posts for? (1-3)

[CHOSEN TOPIC ANALYSIS]
Topic: [What you're posting about]
Target audience: [Who this resonates with]
Tone: [technical/inspirational/practical]

[POST VERSION 1 - LONG FORM]
[Focused narrative post: 250-300 words]

[POST VERSION 2 - SHORT FORM]
[Punchy, concise version: 80-120 words]

[SAVED FOR LATER]
Topics 2 & 3 saved to ~/.claude/post_ideas.json
Use /linkedin-post-generator --upcoming to see all saved ideas
```

## How to Use

**Generate posts from latest session:**
```
/linkedin-post-generator
```

**See all saved post ideas (past sessions):**
```
/linkedin-post-generator --upcoming
```

**Generate a post from a saved idea:**
```
/linkedin-post-generator --id [idea_id]
```

---

## Step-by-Step Instructions for Claude

### Step 1: Find the latest session
Look in `~/.claude/sessions/` for the most recent `.md` file (sorted by date).

### Step 2: Read and analyze the session
Extract all major accomplishments:
- What was built or created
- Key technical decisions
- Problems solved
- Learning insights
- New skills/systems built
- Interesting findings

### Step 3: Identify 2-3 distinct topics
Break down the session into separate, shareable topics. Examples:
- Topic A: "Built Signal Dashboard with AI signal aggregation"
- Topic B: "Integrated Pinecone memory for Claude Code"
- Topic C: "Created post generator skill for automated content"

Each topic should be a **complete narrative** on its own (not dependent on others).

### Step 4: Present options to user
List the 2-3 topics with brief 1-line descriptions.
Ask user: "Which topic would you like to post about? (1-3)"

### Step 5: Generate focused posts for chosen topic
Write 2 versions for the **selected topic only**:

**Version 1 (Long Form - 250-300 words):**
- Hook: Problem statement or insight
- Journey: What you built, how, why
- Impact: Outcome and lesson
- CTA: Question or call-to-action
- 3-5 emojis strategically placed
- Short paragraphs for readability

**Version 2 (Short Form - 80-120 words):**
- Core insight in 1-2 sentences
- Key outcome or learning
- Engagement hook/question
- 2-3 emojis
- Scannable in 10 seconds

### Step 6: Provide posting recommendations
- Suggest when to post (immediately, wait 24-48h, stagger posts, etc.)
- Note if this is part of a series
- Suggest relevant hashtags
- Reference other posts if applicable

### Step 7: Save unused topics
Load `~/.claude/post_ideas.json` (if exists) or create new file.
Add the 1-2 unused topics with:
- Topic name
- Session date
- Session file name
- Brief summary (100 words)
- Suggested posting date (based on staggering)
- Hashtags to use

Append (don't overwrite) so ideas accumulate.

### Step 8: Output formatted posts
Display chosen topic posts in easy copy-paste format with clear headers.
Show filename where unused topics were saved.
Suggest command to view all saved ideas: `/linkedin-post-generator --upcoming`
