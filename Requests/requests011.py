from urllib import response
import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

# Authentication
# When you pass your username and password in a tuple to the 
# auth parameter, requests is applying the credentials using 
# HTTP’s Basic access authentication scheme under the hood.
response = requests.get('https://api.github.com/user', auth=('Yasir323', getpass()))
print(response.status_code)
# Therefore, you could make the same request by passing explicit 
# Basic authentication credentials using HTTPBasicAuth:
requests.get(
    'https://api.github.com/user',
    auth=HTTPBasicAuth('username', getpass())
)