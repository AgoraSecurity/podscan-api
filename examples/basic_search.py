import os

from dotenv import load_dotenv

from podscan_api import PodScanClient

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("PODSCAN_API_KEY")
client = PodScanClient(api_key)


def find_industry_podcasts(industry: str, page: int = 1, per_page: int = 20):
    results = client.podcasts.search(query=industry, page=page, per_page=per_page)
    print(f"Found {len(results['podcasts'])} podcasts related to {industry}:")
    for podcast in results["podcasts"]:
        print(f"- {podcast['podcast_name']}: {podcast['podcast_description'][:100]}...")


if __name__ == "__main__":
    find_industry_podcasts("artificial intelligence security")
