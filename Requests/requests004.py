import requests
from requests.exceptions import HTTPError

# Content
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

print(response.content)
# Because the decoding of bytes to a str requires an encoding 
# scheme, requests will try to guess the encoding based on the 
# response’s headers if you do not specify one. You can provide 
# an explicit encoding by setting .encoding before accessing 
# .text:
print(response.encoding)
print(response.text)

# To get a dictionary, you could take the str you retrieved 
# from .text and deserialize it using json.loads(). However, 
# a simpler way to accomplish this task is to use .json():
print(response.json())
