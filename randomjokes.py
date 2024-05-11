import requests

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        joke = user_data["content"]

        return joke
    else:
        raise Exception("Failed to fetch random jokes")


def main():
    try:
        joke = fetch_random_jokes()
        print(f"Joke: {joke}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()