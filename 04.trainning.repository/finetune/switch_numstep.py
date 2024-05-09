#!/home/cjx/deepmd-kit-2.2.9/bin/python


import json



def read_json(filename):
    '''
    normally read json
    '''

    with open(filename, 'r') as file:
      json_data = json.load(file)

    return json_data


def write_json(filename, json_data):
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=4)


json_data0 = read_json('input.json')

json_data1 = read_json('./init/input-1.json')

for key, value in json_data0.items():
    json_data1["training"][key] = value

write_json('./init/input-1.json',json_data1)

