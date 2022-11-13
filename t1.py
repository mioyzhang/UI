import json


a = {'s': 1,
     'd': 2
     }

s = json.dumps(a)
print(s)
d = json.loads(s)
print(d)