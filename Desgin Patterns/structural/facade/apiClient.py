"""When working with complex APIs that involve multiple endpoints and require authentication, you can use an API
Client Facade to simplify the interaction with the API. The facade can handle authentication, request handling,
error handling, and provide high-level methods that abstract the API's complexity. """

import requests


class APIClientFacade:
    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.auth_token = auth_token

    def _send_request(self, method, endpoint, params=None, data=None):
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        response = requests.request(
            method,
            f"{self.base_url}/{endpoint}",
            params=params,
            data=data,
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    def get_user(self, user_id):
        endpoint = f"users/{user_id}"
        return self._send_request("GET", endpoint)

    def create_user(self, user_data):
        endpoint = "users"
        return self._send_request("POST", endpoint, data=user_data)

    def delete_user(self, user_id):
        endpoint = f"users/{user_id}"
        return self._send_request("DELETE", endpoint)


# Usage
facade = APIClientFacade("https://api.example.com", "auth_token")
user = facade.get_user(123)
print("User:", user)

"""In this example, the APIClientFacade abstracts the complexities of making API requests and handles authentication 
using the provided auth_token. Clients can use the facade methods (get_user(), create_user(), and delete_user()) to 
interact with the API endpoints without directly dealing with the HTTP requests, headers, and error handling. """
