import requests
from requests.exceptions import HTTPError

# Headers
url = 'https://api.github.com/search/repositories'
try:
    response = requests.get(
        url=url,
        params={'q': 'requests+language:python'},
        headers={'Accept': 'application/vnd.github.v3.text-match+json'}
    )
    response.raise_for_status()
except HTTPError as err:
    print(f"HTTPError: {str(err)}")
except Exception as err:
    print(f"{type(err).__name__}: {str(err)}")
else:
    print("Success!")

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')
