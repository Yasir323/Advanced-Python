import csv
import os
from datetime import datetime
import logging
import json
from typing import Any


class MyLogger():
    """Csustom Logger class.
    """

    def __init__(self) -> None:
        # logging = __import__('logging')
        self.cwd = os.getcwd()
        self.current_month = datetime.utcnow().month
        self.current_year = datetime.utcnow().year
        self.logger = logging.getLogger(__name__)
        self.formatter = logging.Formatter('%(levelname)s: %(message)s')

    def get_logger(self, script_name: str, scripts_dir: str = 'python_scripts', stream_handler: bool = False):
        logs_dir = f'{script_name}Logs'
        log_file_name = f'{self.current_month}{self.current_year}.log'
        log_file = os.path.join(self.cwd, scripts_dir, logs_dir, log_file_name)
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)
        if stream_handler:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(self.formatter)
            # stream_handler = logging.StreamHandler(sys.stdout)
            self.logger.addHandler(stream_handler)
        return self.logger
    
    def set_format(self, format: str):
        """Refer documentation for the correct format string.

        Args:
            format (str): Format string.
        """
        self.formatter = logging.Formatter(format)


class CSVReader():

    def __init__(self, filename, header=False) -> None:
        self.filename = filename
        self.header = header

    def read_file(self):
        with open(self.filename, 'rb') as csvfile:
            datareader = csv.reader(csvfile)
            if self.header:
                yield next(datareader)  # yield the header row
            for row in datareader:
                yield row


def to_json(filename: str, object: Any, mode: str = 'w', encoding: str = 'utf-8', indent: int = 4):
    """Save data in JSON format.

    Args:
        filename (str): Path/name of the new file.
        object (Any): The object that needs to be converted to JSON.
        mode (str, optional): Access mode. Defaults to 'w'.
        encoding (str, optional): Encoding format. Defaults to 'utf-8'.
        indent (int, optional): Number of spaces in an indent. Defaults to 4.
    """
    with open(filename, mode, encoding=encoding) as f:
        json.dump(object, f, indent=indent, default=str)
