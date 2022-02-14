import redis
import json
import time

redis_client = redis.StrictRedis(
    host="107.6.175.198",
    # host='127.0.0.1',
    port=7005,
    # port=6379,
    db=0,
    password="nEuV0n3*3",
    charset="utf-8",
    decode_responses=True
)
# LIST
start_time = time.time()
cities = redis_client.zrange('citiesWeatherLookup', 0, -1)
cities_with_forecast = redis_client.hkeys('weatherForecast')
count = 0
for city in cities:
    if city in cities_with_forecast:
        count += 1
print(count)
print(f'List: Time Taken -> {time.time() - start_time}secs.')

# SETS
start_time = time.time()
cities = set(redis_client.zrange('citiesWeatherLookup', 0, -1))
cities_with_forecast = set(redis_client.hkeys('weatherForecast'))
diff = cities.difference(cities_with_forecast)
print(len(cities) - len(diff))
print(f'List: Time Taken -> {time.time() - start_time}secs.')

