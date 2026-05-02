#!/usr/bin/env python3
import os
import json
import sys
from datetime import datetime
from sentence_transformers import SentenceTransformer
import warnings
warnings.filterwarnings('ignore')

try:
    from pinecone import Pinecone

    api_key = os.getenv('PINECONE_API_KEY')
    if not api_key:
        print('Error: PINECONE_API_KEY not set', file=sys.stderr)
        sys.exit(1)

    pc = Pinecone(api_key=api_key)
    index = pc.Index('personal-memory')

    model = SentenceTransformer('nomic-ai/nomic-embed-text-v1')

    summary_text = """Setting up Pinecone memory system & planning signal dashboard skill. Built full Pinecone integration: API key in settings.local.json, pinecone_memory.py script, personal-memory index configured. Tested /recall skill — working and ready. Previous session on signal dashboard skill now retrievable. Next: clarify signal dashboard requirements and discuss data sources (Twitter/X, HN, Reddit, news APIs, RSS)."""

    embedding = model.encode(summary_text)

    # Convert to float list and pad to 1024
    embedding_list = [float(x) for x in embedding.tolist()]
    if len(embedding_list) < 1024:
        embedding_list.extend([0.0] * (1024 - len(embedding_list)))
    elif len(embedding_list) > 1024:
        embedding_list = embedding_list[:1024]

    # Upsert
    session_id = 'session-2026-05-02-0000'
    index.upsert(
        vectors=[(session_id, embedding_list, {'text': summary_text, 'date': '2026-05-02', 'type': 'session'})],
        namespace='default'
    )

    print(f'Saved to memory archive — ID `{session_id}`. Search via `/recall`.')

except Exception as e:
    print(f'Error: {e}', file=sys.stderr)
    sys.exit(1)
