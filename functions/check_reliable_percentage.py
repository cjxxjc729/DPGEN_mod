#!/home/cjx/deepmd-kit-2.2.9/bin/python

import numpy as np
import json
import os

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



# Assuming we're working in a specified directory, here I use the current directory for demonstration.
# You can replace `os.getcwd()` with the path to the target directory.
directory_path = os.getcwd()

# Initialize an empty dictionary to hold the file paths grouped by the ITER variable.
grouped_files = {}

# Walk through the directory to find files that match the criteria.
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith('_af_std.txt'):
            # Construct the relative path from the directory path to the file.
            relative_path = os.path.relpath(os.path.join(root, file), directory_path)
            # Split the relative path to get the ITER variable, which is the second character after splitting by '/'.
            parts = relative_path.split('/')
            # For the purpose of this task, we assume that 'parts' has enough elements to get the second segment.
            if len(parts) > 1:
                iter_var = parts[0]  # Get the second character of the second part
                # Group files by the ITER variable.
                if iter_var not in grouped_files:
                    grouped_files[iter_var] = []
                grouped_files[iter_var].append(relative_path)


# Assuming grouped_files is your dictionary
for key, value in reversed(list(grouped_files.items())):
    print("-----------",key,"-------------------")
    home_dir=os.getcwd()

    resutls_good_med_bad=[]
    fs_af_std = value
    stds = []
    for f_af_std in fs_af_std:
        std = np.loadtxt(f_af_std)[:,1]
        stds = np.append(stds,std)

    os.chdir(key)
    json_data = read_json('input.json')
    #model_dev_high_bound = json_data["02.selection"]["parameters"]["model_dev_high_bound"]
    #model_dev_low_bound  = json_data["02.selection"]["parameters"]["model_dev_low_bound"]
    model_dev_high_bound = 0.4
    model_dev_low_bound = 0.2
    print("stds=",stds)
    ngood = len(np.where(stds < model_dev_low_bound)[0])
    nmed  = len(np.where((stds <= model_dev_high_bound) & (stds >= model_dev_low_bound))[0])
    nbad  = len(np.where(stds > model_dev_high_bound)[0])
    print("====ngood  nmed  nbad ====")
    print(ngood,nmed,nbad)

    os.chdir(home_dir)
