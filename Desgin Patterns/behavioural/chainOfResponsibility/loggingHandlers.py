"""In a logging system, you can use the Chain of Responsibility pattern to handle different levels of log messages.
Each handler in the chain can be responsible for logging messages of a specific severity level, such as INFO,
WARNING, or ERROR. The log messages can be passed through the chain, and each handler can choose to handle the
message or pass it to the next handler. This allows for flexible logging configurations, where you can dynamically
add or remove handlers based on the desired log level or specific logging requirements. """

import logging


class LogLevelHandler:
    def __init__(self, level, successor=None):
        self.level = level
        self.successor = successor

    def handle_log(self, level, message):
        if level == self.level:
            logging.log(level, message)
        elif self.successor is not None:
            self.successor.handle_log(level, message)


# Usage
handler = LogLevelHandler(logging.INFO,
                          LogLevelHandler(logging.WARNING,
                                          LogLevelHandler(logging.ERROR)))

handler.handle_log(logging.WARNING, "This is a warning message.")
handler.handle_log(logging.DEBUG, "This is a debug message.")
