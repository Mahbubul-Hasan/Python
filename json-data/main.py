import json

a = {
    'name': 'Max',
    'age': 22,
    'markes': [90, 80, 70, 60, 50],
    'pass': True,
    'object':{
        'color': ['Red, Blue']
    }
}

print(json.dumps(a))
print(json.dumps(a, indent=3))
print(json.dumps(a, indent=3, sort_keys=True))

fileHandling = open('json-data/test.json', 'w')
fileHandling.write(json.dumps(a, indent=3))
fileHandling.close()

fileHandling = open('json-data/test.json', 'r')
print(fileHandling.read())
# -------------------------------
jeson_value = json.loads(fileHandling.read())
print(jeson_value)
print(jeson_value['name'])
# -------------------------------
fileHandling.close()
