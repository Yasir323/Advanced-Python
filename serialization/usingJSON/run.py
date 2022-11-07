"""Basic usage of JSON"""
import json

"""Shopping event"""
from datetime import datetime


def default(obj):
    """Encode datetime to string in YYYY-MM-DDTHH:MM:SS format (RFC3339)"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj


def pairs_hook(pairs):
    """Convert the "time" key to datetime"""
    obj = {}
    for key, value in pairs:
        if key == 'time':
            value = datetime.fromisoformat(value)  # Python >= 3.7
        obj[key] = value
    return obj


event = {
    'time': datetime(2020, 4, 17, 13, 27, 48),
    'name': 'Homer',
    'item': 'Duff',
    'amount': 4,
    'item price': 4.75,
}

# Serialize to bytes, dict keys must be str
data = json.dumps(event, default=default)
print('serialized:', data)
print('data type:', type(data))
data_bytes = data.encode('utf-8')
print('data_bytes type:', type(data_bytes))

# Indent
print('serialized indented:', json.dumps(event, indent=4, default=default))

event_str = json.loads(data, object_pairs_hook=pairs_hook)
print('equal:', event_str == event)

event_bytes = json.loads(data_bytes)  # Can loads from bytes as well
print('equal (bytes):', event_bytes == event)

# Working with files
with open('event.json', 'w') as out:
    json.dump(event, out, indent=4, default=default)

with open('event.json') as fp:
    event_file = json.load(fp, object_pairs_hook=pairs_hook)

print('equal (file):', event_file == event)
