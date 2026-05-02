#!/usr/bin/env python3
import os
import sys
import json
import argparse

try:
    from pinecone import Pinecone
except ImportError:
    print("Error: pinecone package not installed. Install with: pip install pinecone", file=sys.stderr)
    sys.exit(1)

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Error: sentence-transformers package not installed. Install with: pip install sentence-transformers", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Query Pinecone memory index")
    parser.add_argument("command", choices=["query"], help="Command to run")
    parser.add_argument("query_text", help="Query text")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results to return")
    parser.add_argument("--index", default="personal-memory", help="Pinecone index name")

    args = parser.parse_args()

    # Get API key from environment
    api_key = os.getenv("PINECONE_API_KEY")
    if not api_key:
        print("Error: PINECONE_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    # Initialize Pinecone
    pc = Pinecone(api_key=api_key)
    index = pc.Index(args.index)

    # Load embedding model (using Nomic for 768 dimensions, will pad to 1024)
    model = SentenceTransformer("nomic-ai/nomic-embed-text-v1")

    # Generate embedding for query
    query_embedding = model.encode(args.query_text).tolist()

    # Pad embedding to 1024 dimensions if needed
    if len(query_embedding) < 1024:
        query_embedding.extend([0] * (1024 - len(query_embedding)))
    elif len(query_embedding) > 1024:
        query_embedding = query_embedding[:1024]

    # Query Pinecone
    results = index.query(
        vector=query_embedding,
        top_k=args.top_k,
        include_metadata=True
    )

    # Format and print results
    if args.command == "query":
        print(json.dumps({
            "query": args.query_text,
            "results": results.get("matches", [])
        }, indent=2))


if __name__ == "__main__":
    main()
