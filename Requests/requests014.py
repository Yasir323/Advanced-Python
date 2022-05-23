import requests
from getpass import getpass

# SESSIONS

# Each time you make a request with session, once it has 
# been initialized with authentication credentials, the 
# credentials will be persisted.

# By using a context manager, you can ensure the resources used by
# the session will be released after use
with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')

# The primary performance optimization of sessions comes in the 
# form of persistent connections. When your app makes a connection 
# to a server using a Session, it keeps that connection around in 
# a connection pool. When your app wants to connect to the same 
# server again, it will reuse a connection from the pool rather 
# than establishing a new one.

# You can inspect the response just like you did before
print(response.headers)
print(response.json())
