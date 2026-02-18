import requests

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your CricAPI key
URL = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0"

def get_latest_scores():
    try:
        response = requests.get(URL)
        data = response.json()

        if data["status"] != "success":
            print("Failed to fetch match data.")
            return

        matches = data.get("data", [])

        if not matches:
            print("No live matches found.")
            return

        print("\n=== Latest Cricket Match Scores ===\n")

        for match in matches:
            print(f"Match: {match.get('name', 'N/A')}")
            print(f"Status: {match.get('status', 'N/A')}")

            scores = match.get("score", [])
            for s in scores:
                print(f"{s.get('inning')}: {s.get('r')}/{s.get('w')} ({s.get('o')} overs)")

            print("-" * 50)

    except Exception as e:
        print("Error fetching scores:", e)

if __name__ == "__main__":
    get_latest_scores()
