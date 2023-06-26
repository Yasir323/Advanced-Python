"""In a chatroom application, the Mediator pattern can be used to facilitate communication between multiple users.
The mediator acts as a central hub that receives messages from users and broadcasts them to all other users in the
chatroom. """


class ChatroomMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, sender, message):
        for user in self.users:
            if user != sender:
                user.receive_message(sender, message)


class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom

    def send_message(self, message):
        self.chatroom.send_message(self, message)

    def receive_message(self, sender, message):
        print(f"{self.name} received a message from {sender.name}: {message}")


# Usage
chatroom = ChatroomMediator()

user1 = User("John", chatroom)
user2 = User("Jane", chatroom)
user3 = User("Alice", chatroom)

chatroom.add_user(user1)
chatroom.add_user(user2)
chatroom.add_user(user3)

user1.send_message("Hello, everyone!")
