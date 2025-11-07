import json

data = '{"name": "Bob", "age": 30}'

try:
    obj = json.loads(data + ',')
    print(obj['name'])
except json.JSONDecodeError:
    print("Ошибка JSONDecodeError")