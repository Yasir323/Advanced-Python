import logging


class LoggerFactory:
    """
    A logger factory that creates different loggers based on a given log level
    or destination. This allows you to switch between different logging
    strategies without modifying the client code.
    """

    @staticmethod
    def create_logger(log_level):
        _logger = logging.getLogger()
        _logger.setLevel(log_level)
        return _logger


# Usage
factory = LoggerFactory()
logger = factory.create_logger(logging.INFO)
logger.info("This is an information log message.")
