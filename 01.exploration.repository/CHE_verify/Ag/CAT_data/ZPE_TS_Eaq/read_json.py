#!/home/cjx/deepmd-kit-2.2.9/bin/python

import sys
import json

# Path to the corrected JSON file
file_path = sys.argv[1]

# Read the JSON data from the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Now, `data` contains the JSON object which you can use as needed
print(data)

