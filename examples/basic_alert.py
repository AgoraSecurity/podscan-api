import os

from dotenv import load_dotenv

from podscan_api import PodScanClient

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("PODSCAN_API_KEY")
client = PodScanClient(api_key)


def create_company_mention_alert(team_id: str, company_name: str):
    alert_data = {
        "alert_name": f"{company_name} Mentions",
        "prompt_filters": [company_name],
        "notification_email": "alerts@yourcompany.com",
        "notification_summary_enabled": True,
        "notification_summary_frequency": "daily",
    }
    result = client.alerts.create(team_id, alert_data)
    print(
        f"Alert created: {result['alert']['alert_name']} (ID: {result['alert']['alert_id']})"
    )


if __name__ == "__main__":
    my_team = client.teams.list()
    print(
        f"Creating an alert for team: {my_team['teams'][0]['team_name']} for company: AgoraSecurity"
    )
    create_company_mention_alert(my_team["teams"][0]["team_id"], "AgoraSecurity")
