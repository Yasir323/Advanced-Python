import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        # If response was successful, no excetion raised
        response.raise_for_status()
    except HTTPError as err:
        print(f"HTTPError: {str(err)}")
    except Exception as err:
        print(f"{type(err).__name__}: {str(err)}")
    else:
        print("Success!")

