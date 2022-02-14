import logging

log_file = 'test.log'
# Set up Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s: %(message)s')
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

try:
    logger.info('FIRST', 'SECOND')
    print('Can you print it?')
    logger.info('Can you print it?')
except Exception as e:
    template = "An exception of type {0} occurred.\nMessage:{1!r}"
    message = template.format(type(e).__name__, e.args)
    logger.exception(message)
finally:
    print('Finally')
    logger.info('Finally')