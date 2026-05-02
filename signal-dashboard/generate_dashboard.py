#!/usr/bin/env python3
"""
Generate HTML dashboard from signal data.
Takes JSON signal data and produces a browsable dashboard.
"""

import json
import os
from datetime import datetime

TEMPLATE_PATH = os.path.dirname(__file__) + "/dashboard_template.html"
OUTPUT_DIR = os.path.expanduser("~/.claude/signal_dashboard/output")

def ensure_output_dir():
    """Create output directory if it doesn't exist"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def sentiment_color(sentiment):
    """Map sentiment to HTML color"""
    colors = {
        "Excited": "#10b981",      # Green
        "Skeptical": "#f59e0b",    # Amber
        "Mixed": "#8b5cf6",        # Purple
        "Neutral": "#6b7280"       # Gray
    }
    return colors.get(sentiment, "#6b7280")

def generate_dashboard(signals_json_path, content_outlines_json_path=None):
    """
    Generate HTML dashboard from signals.

    Args:
        signals_json_path: Path to JSON file with fetched signals
        content_outlines_json_path: Optional path to JSON file with Claude-generated outlines
    """

    ensure_output_dir()

    # Load signals
    with open(signals_json_path, encoding="utf-8") as f:
        data = json.load(f)

    signals = data.get("signals", [])[:10]  # Top 10

    # Load template
    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        template = f.read()

    # Build signals HTML
    signals_html = ""
    for signal in signals:
        relevance = signal.get("relevance_score", 0)
        adopter = signal.get("early_adopter_score", 0)
        relevance_pct = (relevance / 10) * 100
        adopter_pct = (adopter / 10) * 100

        signals_html += f"""
        <div class="signal">
            <div class="signal-header">
                <div>
                    <h3 class="signal-title">{signal["title"]}</h3>
                </div>
                <span class="signal-source">{signal["source"]}</span>
            </div>

            {f'<p class="signal-description">{signal["description"]}</p>' if signal.get("description") else ''}

            <div class="signal-metrics">
                <div class="metric">
                    <div class="metric-label">Relevance Score</div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="--progress-width: {relevance_pct}%; width: {relevance_pct}%;"></div>
                    </div>
                    <div class="metric-value">{relevance}/10</div>
                </div>
                <div class="metric">
                    <div class="metric-label">Early Adopter Momentum</div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="--progress-width: {adopter_pct}%; width: {adopter_pct}%;"></div>
                    </div>
                    <div class="metric-value">{adopter}/10</div>
                </div>
            </div>

            <div class="signal-footer">
                <a href="{signal["url"]}" target="_blank" class="signal-link">View Source →</a>
            </div>
        </div>
        """

    # Get current time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Render template
    html = template.replace("{{ SIGNALS }}", signals_html).replace("{{ TIMESTAMP }}", now)

    # Save to file
    today = datetime.now().strftime("%Y-%m-%d")
    output_path = os.path.join(OUTPUT_DIR, f"{today}.html")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[OK] Dashboard generated: {output_path}")
    return output_path

if __name__ == "__main__":
    # For testing - expects signals.json in same directory
    import sys
    if len(sys.argv) > 1:
        generate_dashboard(sys.argv[1])
    else:
        print("Usage: python generate_dashboard.py <signals_json_path>")
