##JSON Data parsing
import json
input = '''[
        {"id":"001",
        "x":"2",
        "name":"chuck"
        },
        {"id":"009",
        "x":"7",
        "name":"Jeevan"
        }
]'''
info = json.loads(input)
print('User Count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('ID:', item['id'])
    print('Attribute:', item['x'])
