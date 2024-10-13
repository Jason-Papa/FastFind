import requests

def find_synonyms(word, limit = 10):
    try:
        # Thesaurus.com API URL that fetches synonym data
        url = f"https://tuna.thesaurus.com/pageData/{word}"

        # Send an HTTP request to fetch the JSON response
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve synonyms for '{word}' (status code {response.status_code}).")
            return
        
        # Parse the JSON response
        data = response.json()

        # Extract synonyms from the JSON data
        try:
            synonym_list = data['data']['definitionData']['definitions'][0]['synonyms']
            synonyms = [syn['term'] for syn in synonym_list]

            print(f"Synonyms for '{word}':")
            limit = min(len(synonyms), limit)
            for synonym in synonyms[:limit]:
                print(f"- {synonym}")
        except KeyError:
            print(f"No synonyms found for '{word}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
