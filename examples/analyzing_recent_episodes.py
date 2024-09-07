import os
from datetime import datetime, timezone
from typing import Dict, List

from dotenv import load_dotenv

from podscan_api import PodScanClient

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("PODSCAN_API_KEY")
client = PodScanClient(api_key)


def format_duration(seconds: int) -> str:
    minutes, secs = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"
    else:
        return f"{minutes}m {secs}s"


def format_date(date_string: str) -> str:
    date = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
    return date.astimezone(timezone.utc).strftime("%B %d, %Y at %I:%M %p UTC")


def analyze_recent_episodes(num_episodes: int = 10) -> List[Dict]:
    episodes = client.episodes.get_recent(per_page=num_episodes)

    analyzed_episodes = []
    for episode in episodes["episodes"]:
        analyzed_episode = {
            "title": episode["episode_title"],
            "podcast": episode["podcast"]["podcast_name"],
            "posted_at": format_date(episode["posted_at"]),
            "duration": format_duration(episode["episode_duration"]),
            "description": (
                episode["episode_description"][:100] + "..."
                if len(episode["episode_description"]) > 100
                else episode["episode_description"]
            ),
            "url": episode["episode_url"],
        }
        analyzed_episodes.append(analyzed_episode)

    return analyzed_episodes


def display_episodes(episodes: List[Dict]):
    print(f"Analyzed {len(episodes)} recent episodes\n")

    for i, episode in enumerate(episodes, 1):
        print(f"Episode {i}:")
        print(f"Title: {episode['title']}")
        print(f"Podcast: {episode['podcast']}")
        print(f"Posted: {episode['posted_at']}")
        print(f"Duration: {episode['duration']}")
        print(f"Description: {episode['description']}")
        print(f"URL: {episode['url']}")
        print("-" * 80)


if __name__ == "__main__":
    recent_episodes = analyze_recent_episodes()
    display_episodes(recent_episodes)
