import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        return response.json()
    else:
        return {}
    

if __name__ == "__main__":
    post = fetch_data()
    print("fetched post title:", post.get("title", "No title found"))