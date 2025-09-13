import json

data = {
    "users": [
        {"id": "U1", "name": "Alice", "age": 25},
        {"id": "U2", "name": "Bob", "age": 30}
    ]
}

print(json.dumps(data))
