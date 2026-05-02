#!/usr/bin/env python3
"""
Signal Dashboard - Fetch signals from multiple AI/automation sources.
Runs in parallel to gather signals from HN, ArXiv, GitHub, and Reddit.
"""

import json
import requests
import feedparser
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
import os

# Load config
CONFIG_PATH = os.path.dirname(__file__) + "/config.json"
with open(CONFIG_PATH) as f:
    CONFIG = json.load(f)

class Signal:
    """Represents a single signal (news item, paper, etc)"""
    def __init__(self, title, url, source, score=0, age_hours=0, description=""):
        self.title = title
        self.url = url
        self.source = source
        self.score = score
        self.age_hours = age_hours
        self.description = description
        self.relevance_score = 0
        self.early_adopter_score = 0

    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "source": self.source,
            "score": self.score,
            "age_hours": self.age_hours,
            "description": self.description,
            "relevance_score": self.relevance_score,
            "early_adopter_score": self.early_adopter_score
        }

def is_relevant(text):
    """Check if text contains AI/automation keywords"""
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in CONFIG["keywords"])

def calculate_relevance_score(title, description=""):
    """Score how relevant this is to AI/automation for builders"""
    text = (title + " " + description).lower()
    count = sum(1 for keyword in CONFIG["keywords"] if keyword.lower() in text)
    return min(count, 10)  # Max score 10

def fetch_hacker_news():
    """Fetch top AI/automation stories from Hacker News"""
    signals = []
    try:
        # Get top 30 stories
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        top_stories = requests.get(url, timeout=5).json()[:30]

        for story_id in top_stories:
            try:
                story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
                story = requests.get(story_url, timeout=3).json()

                if not story or "title" not in story:
                    continue

                title = story.get("title", "")
                if not is_relevant(title):
                    continue

                signal = Signal(
                    title=title,
                    url=story.get("url", f"https://news.ycombinator.com/item?id={story_id}"),
                    source="Hacker News",
                    score=story.get("score", 0),
                    age_hours=0,
                    description=""
                )
                signal.relevance_score = calculate_relevance_score(title)
                signal.early_adopter_score = min(10, signal.score // 10)
                signals.append(signal)
            except:
                continue
    except Exception as e:
        print(f"Warning: HN fetch failed: {e}")

    return signals

def fetch_arxiv():
    """Fetch recent papers from ArXiv"""
    signals = []
    try:
        categories = "+OR+".join(CONFIG["arxiv_categories"])
        url = f"http://arxiv.org/rss/{categories}"
        feed = feedparser.parse(url)

        now = datetime.now()
        for entry in feed.entries[:20]:
            title = entry.get("title", "")
            published = entry.get("published", "")

            if not is_relevant(title):
                continue

            # Calculate age
            try:
                pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
                age_hours = (now - pub_date).total_seconds() / 3600
            except:
                age_hours = 0

            signal = Signal(
                title=title,
                url=entry.get("link", ""),
                source="ArXiv",
                score=0,
                age_hours=age_hours,
                description=entry.get("summary", "")[:200]
            )
            signal.relevance_score = calculate_relevance_score(title, signal.description)
            signal.early_adopter_score = 10 if age_hours < 12 else 5  # Fresh papers score high
            signals.append(signal)
    except Exception as e:
        print(f"Warning: ArXiv fetch failed: {e}")

    return signals

def fetch_github():
    """Fetch trending AI repos from GitHub"""
    signals = []
    try:
        keywords = " OR ".join([f'"{kw}"' for kw in ["AI", "LLM", "automation", "agent", "model"]])
        url = f"https://api.github.com/search/repositories?q={keywords}&sort=stars&order=desc&per_page=20"

        response = requests.get(url, timeout=5)
        repos = response.json().get("items", [])

        for repo in repos:
            title = repo.get("name", "")
            full_name = repo.get("full_name", "")
            description = repo.get("description", "")

            if not is_relevant(title + " " + (description or "")):
                continue

            # Star velocity (stars gained today roughly)
            stars = repo.get("stargazers_count", 0)

            signal = Signal(
                title=f"{full_name}: {description or title}",
                url=repo.get("html_url", ""),
                source="GitHub",
                score=stars,
                age_hours=0,
                description=description or ""
            )
            signal.relevance_score = calculate_relevance_score(title, description or "")
            signal.early_adopter_score = min(10, max(5, stars // 100))  # Higher stars = early adopter signal
            signals.append(signal)
    except Exception as e:
        print(f"Warning: GitHub fetch failed: {e}")

    return signals

def fetch_reddit():
    """Fetch discussions from AI/automation subreddits"""
    signals = []
    try:
        for subreddit in CONFIG["subreddits"]:
            try:
                url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                headers = {"User-Agent": "signal-dashboard/1.0"}
                response = requests.get(url, headers=headers, timeout=5)
                posts = response.json().get("data", {}).get("children", [])

                for post in posts[:10]:
                    post_data = post.get("data", {})
                    title = post_data.get("title", "")

                    if not is_relevant(title):
                        continue

                    signal = Signal(
                        title=title,
                        url=f"https://reddit.com{post_data.get('permalink', '')}",
                        source=f"Reddit r/{subreddit}",
                        score=post_data.get("score", 0),
                        age_hours=0,
                        description=post_data.get("selftext", "")[:200]
                    )
                    signal.relevance_score = calculate_relevance_score(title, signal.description)
                    signal.early_adopter_score = min(10, signal.score // 50)
                    signals.append(signal)
            except Exception as e:
                print(f"Warning: Reddit r/{subreddit} fetch failed: {e}")
    except Exception as e:
        print(f"Warning: Reddit fetch failed: {e}")

    return signals

def fetch_all_signals():
    """Fetch signals from all sources in parallel"""
    signals = []

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(fetch_hacker_news): "Hacker News",
            executor.submit(fetch_arxiv): "ArXiv",
            executor.submit(fetch_github): "GitHub",
            executor.submit(fetch_reddit): "Reddit"
        }

        for future in as_completed(futures):
            try:
                source_signals = future.result()
                signals.extend(source_signals)
            except Exception as e:
                print(f"Error fetching signals: {e}")

    return signals

def rank_signals(signals):
    """Rank signals by relevance + early adopter score"""
    # Combined score = 60% relevance + 40% early adopter
    for signal in signals:
        signal.combined_score = (signal.relevance_score * 0.6) + (signal.early_adopter_score * 0.4)

    return sorted(signals, key=lambda s: s.combined_score, reverse=True)

if __name__ == "__main__":
    print("Fetching signals...")
    signals = fetch_all_signals()
    ranked = rank_signals(signals)

    print(f"\nFetched {len(signals)} signals from all sources")
    print("\nTop 10 signals:")
    for i, signal in enumerate(ranked[:10], 1):
        try:
            print(f"{i}. [{signal.source}] {signal.title}")
            print(f"   Score: {signal.combined_score:.1f} (Relevance: {signal.relevance_score}, Early Adopter: {signal.early_adopter_score})")
            print(f"   {signal.url}\n")
        except UnicodeEncodeError:
            # Handle unicode errors on Windows
            print(f"{i}. [{signal.source}] [Title with unicode - see JSON]")

    # Output JSON for Claude to process
    output = {
        "timestamp": datetime.now().isoformat(),
        "total_signals": len(signals),
        "signals": [s.to_dict() for s in ranked]
    }

    print("\nJSON OUTPUT FOR CLAUDE:")
    print(json.dumps(output, indent=2))
