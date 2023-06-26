"""In scenarios where you need to access a remote API or web service, the Proxy pattern can be used to encapsulate
the communication details and provide a convenient interface for clients. The proxy handles network requests,
authentication, and other necessary operations, shielding the client from the complexities of remote communication. """

import requests


class RemoteAPI:
    def get_data(self):
        response = requests.get("https://api.example.com/data")
        return response.json()


class APIProxy:
    def __init__(self):
        self.remote_api = RemoteAPI()

    def get_data(self):
        # Perform additional operations before or after accessing the remote API
        print("Performing pre-processing steps...")
        data = self.remote_api.get_data()
        print("Performing post-processing steps...")
        return data


# Usage
proxy = APIProxy()
data = proxy.get_data()
print(data)
