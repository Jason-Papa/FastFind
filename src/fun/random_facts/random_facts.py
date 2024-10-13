import requests

def generate_random_fact():
    try:
        response = requests.get(
            "https://uselessfacts.jsph.pl/random.json?language=en"
        )
        print(response.json()["text"])
    except Exception as e:
        print("Error,", e)
