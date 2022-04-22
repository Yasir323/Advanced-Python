from dataclasses import dataclass


@dataclass
class Location:
    name: str
    lon: float = 0.0
    lat: float = 0.0


print(Location('Null Island'))
print(Location('Greenwich', lat=51.8))
print(Location(('Vancouver', -123.1, 49.3)))
