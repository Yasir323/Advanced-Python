import requests
from requests.exceptions import HTTPError

# Headers
url = 'https://api.github.com'
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

# The response headers can give you useful information, such 
# as the content type of the response payload and a time limit 
# on how long to cache the response. To view these headers, 
# access .headers:
print(response.headers)

# .headers returns a dictionary-like object, allowing you to 
# access header values by key. For example, to see the content 
# type of the response payload, you can access Content-Type:
print(response.headers['content-type'])
