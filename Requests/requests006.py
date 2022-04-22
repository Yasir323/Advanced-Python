import requests
from requests.exceptions import HTTPError

# Query String Paramenters
url = 'https://api.github.com/search/repositories'
try:
    response = requests.get(
        url=url,
        params={'q': 'requests+language:python'}
        # params=[('q': 'requests+language:python')]
        # params=b'q=requests+language:python'
    )
    # You can pass params to get() in the form of a dictionary, 
    # as you have just done, or as a list of tuples or even as bytes.
    response.raise_for_status()
except HTTPError as err:
    print(f"HTTPError: {str(err)}")
except Exception as err:
    print(f"{type(err).__name__}: {str(err)}")
else:
    print("Success!")

