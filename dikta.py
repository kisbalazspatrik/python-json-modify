import os.path
import json

filename = 'from.json'

jsonArr = []

with open(filename) as data_file:
    data = json.load(data_file)

for x in range(640):
    file_exists = os.path.exists(f'{x}.gif')
    if file_exists:
        data[x]['Customized'] = 'Yes'

jsonArr.append(data)
with open("to.json", "w") as outf:
    json.dump(jsonArr, outf, indent=4)