import time


class CacheManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.cache = {}
        return cls._instance

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value


# Usage in the web application
def get_data_from_api(api_endpoint):
    # Check if data is present in the cache
    cached_data = CacheManager().get(api_endpoint)
    if cached_data:
        return cached_data

    # Make API call to retrieve data
    api_response = make_api_call(api_endpoint)
    data = process_api_response(api_response)

    # Cache the data for future use
    CacheManager().set(api_endpoint, data)

    return data


def make_api_call(endpoint):
    print(endpoint)
    return "Hi"


def process_api_response(data):
    time.sleep(0.1)
    return data


# Request 1
data1 = get_data_from_api('/users')  # API call is made, data is retrieved and cached

# Request 2 (within a short time frame)
data2 = get_data_from_api('/users')  # Data is retrieved from the cache, no API call is made

# Request 3 (after cache expiration or eviction)
data3 = get_data_from_api('/users')  # API call is made again, new data is retrieved and cached
