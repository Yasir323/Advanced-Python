"""Load configuration with importlib"""
from importlib.machinery import SourceFileLoader


def load_config(path):
    """Load configuration from path"""
    return SourceFileLoader('config', path).load_module()


if __name__ == '__main__':
    config = load_config('serverConfiguration.py')
    print(config)
    print(config.api_key)
