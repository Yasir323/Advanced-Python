class User:
    def __init__(self, username):
        self.username = username

    def get_details(self):
        return f"Username: {self.username}"


class NullUser:
    def get_details(self):
        return "No user found"


def user_exists_in_database(username, results):
    return username in results


# Usage
def fetch_user_from_database(username):
    results = {}
    # Database query logic
    if user_exists_in_database(username, results):
        return User(username)
    else:
        return NullUser()


user1 = fetch_user_from_database("john")
user2 = fetch_user_from_database("mary")

print(user1.get_details())  # Username: john
print(user2.get_details())  # No user found
