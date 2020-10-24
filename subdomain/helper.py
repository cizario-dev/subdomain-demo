import json

with open('names.txt', 'r') as f:
    lines = [l.replace('\n','') for l in f.readlines()]

output=[]

for i, val in enumerate(lines):
    elem = {
        "model": "home.Contact",
        "pk": i+1,
        "fields": {
            "first_name": val[0],
            "last_name": val[1]
        },
    }
    output.append(elem)

with open('contact-fixtures.json', 'w') as f:
    json.dump(output, f)