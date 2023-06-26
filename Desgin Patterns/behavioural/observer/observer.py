# The base publisher class includes subscription management
# code and notification methods.
class EventManager:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, eventType, listener):
        if eventType not in self.listeners:
            self.listeners[eventType] = []
        self.listeners[eventType].append(listener)

    def unsubscribe(self, eventType, listener):
        if eventType in self.listeners:
            self.listeners[eventType].remove(listener)

    def notify(self, eventType, data):
        if eventType in self.listeners:
            for listener in self.listeners[eventType]:
                listener.update(data)


# The concrete publisher contains real business logic that's
# interesting for some subscribers. We could derive this class
# from the base publisher, but that isn't always possible in
# real life because the concrete publisher might already be a
# subclass. In this case, you can patch the subscription logic
# in with composition, as we did here.
class Editor:
    def __init__(self):
        self.events = EventManager()
        self.file = None

    # Methods of business logic can notify subscribers about
    # changes.
    def openFile(self, path):
        self.file = File(path)
        self.events.notify("open", self.file.name)

    def saveFile(self):
        self.file.write()
        self.events.notify("save", self.file.name)

    # ...


# Here's the subscriber interface. If your programming language
# supports functional types, you can replace the whole
# subscriber hierarchy with a set of functions.
class EventListener:
    def update(self, filename):
        pass


# Concrete subscribers react to updates issued by the publisher
# they are attached to.
class LoggingListener(EventListener):
    def __init__(self, log_filename, message):
        self.log = File(log_filename)
        self.message = message

    def update(self, filename):
        self.log.write(self.message.replace('%s', filename))


class EmailAlertsListener(EventListener):
    def __init__(self, email, message):
        self.email = email
        self.message = message

    def update(self, filename):
        system.email(self.email, self.message.replace('%s', filename))


# An application can configure publishers and subscribers at
# runtime.
class Application:
    def config(self):
        editor = Editor()

        logger = LoggingListener(
            "/path/to/log.txt",
            "Someone has opened the file: %s")
        editor.events.subscribe("open", logger)

        emailAlerts = EmailAlertsListener(
            "admin@example.com",
            "Someone has changed the file: %s")
        editor.events.subscribe("save", emailAlerts)
