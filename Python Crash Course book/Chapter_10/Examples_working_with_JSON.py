# Using Python's JSON Module

import json

numbers = [2, 3, 5, 7, 11, 13]

with open('filename.json', 'w') as f:
    json.dump(numbers, f)

    # Using json.dump we can add stuff to the file

# WE use json.load to read data back from a json file

with open('filename.json') as f:
    datas = json.load(f)
    for data in datas:
        print(data)