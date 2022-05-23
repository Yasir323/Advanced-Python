from dataclasses import dataclass, field, fields
from typing import Union


@dataclass
class Location:
    name: Union[str, int]
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})


# The metadata (and other information about a field) can be 
# retrieved using the fields() function (note the plural s):
print(fields(Location))
