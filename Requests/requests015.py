import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

# Max Retries
# When a request fails, you may want your application to 
# retry the same request. However, requests will not do 
# this for you by default. To apply this functionality, 
# you need to implement a custom Transport Adapter.

# Transport Adapters let you define a set of configurations 
# per service you’re interacting with. For example, let’s 
# say you want all requests to https://api.github.com to 
# retry three times before finally raising a ConnectionError. 
# You would build a Transport Adapter, set its max_retries 
# parameter, and mount it to an existing Session:
github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# Use `github_adapter` for all requests to endpoints that start with this URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)
# When you mount the HTTPAdapter, github_adapter, to session, session 
# will adhere to its configuration for each request to https://api.github.com.
