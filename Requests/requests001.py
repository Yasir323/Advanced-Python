import requests

response = requests.get('https://api.github.com')
# If you want to disable SSL Certificate verification, you pass 
# False to the verify parameter of the request function:
# response = requests.get('https://api.github.com', verify=False)

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

print(response.text)
