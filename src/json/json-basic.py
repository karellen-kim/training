import json

# from file
f = open("json-test.json", "r")
datas = json.loads(f.read())
print(datas)
