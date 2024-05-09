#!/home/cjx/deepmd-kit-2.2.9/bin/python

import json 
import sys
from ase.io import read,write
import os

def read_json(filename):
    with open(filename, 'r') as file:
      json_data = json.load(file)

    return json_data


def write_json(filename, json_data):
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=4)


json_data = read_json('../input.json')

element_pun_from = json_data['element_pun_from']
element_pun_to = json_data['element_pun_to']

fs=os.listdir('./')
fs.sort()
fs_cif=[]
for f in fs:
    if f.endswith('.cif'):
        fs_cif.append(f)

for f_cif in fs_cif:

    atoms=read(f_cif)

    element_pun_from_index = [atom.index for atom in atoms if atom.symbol == element_pun_from]
    #print(element_pun_from_index)

    if len(element_pun_from_index) != 0 :
        atoms.symbols[element_pun_from_index] = element_pun_to
        write(f_cif,atoms)
