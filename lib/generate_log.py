from datetime import datetime
import requests


def generate_log(log_data):
    """
    Creates a log file from a list of log entries.
    Returns the filename.
    """

    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename


def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


if __name__ == "__main__":
    logs = [
        "User logged in",
        "User updated profile",
        "Report exported",
    ]

    filename = generate_log(logs)
    print(f"Log written to {filename}")

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))