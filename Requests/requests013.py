import requests
from requests.exceptions import Timeout

# Perfromance
# When you make an inline request to an external service, 
# your system will need to wait upon the response before 
# moving on. If your application waits too long for that 
# response, requests to your service could back up, your 
# user experience could suffer, or your background jobs 
# could hang.

# By default, requests will wait indefinitely on the response, 
# so you should almost always specify a timeout duration to 
# prevent these things from happening. To set the request’s 
# timeout, use the timeout parameter. timeout can be an 
# integer or float representing the number of seconds to wait 
# on a response before timing out:
response = requests.get('https://api.github.com', timeout=1)
# You can also pass a tuple to timeout with the first element 
# being a connect timeout (the time it allows for the client to 
# establish a connection to the server), and the second being a 
# read timeout (the time it will wait on a response once your 
# client has established a connection):
response = requests.get('https://api.github.com', timeout=(1, 3))
# If the request establishes a connection within 1 seconds and 
# receives data within 3 seconds of the connection being established, 
# then the response will be returned as it was before. If the 
# request times out, then the function will raise a Timeout 
# exception:
try:
    response = requests.get('https://api.github.com', timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

print(response.text)
