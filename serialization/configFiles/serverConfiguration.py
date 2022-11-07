import logging
import sys
import os

api_key = os.environ.get('API_KEY') or 'test-api-key'
logging_level = logging.INFO
port = 8080

if sys.platform == 'win32':
    num_workers = 10
else:
    num_workers = 100

# Cleanup
# del __doc__
del logging
del sys
del os
