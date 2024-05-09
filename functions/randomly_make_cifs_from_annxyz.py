#!/home/cjx/deepmd-kit-2.2.9/bin/python

import sys

from ase.io import write
from ase.io import read
from ase import neighborlist
from ase import geometry
import numpy as np
from mimic_functions import *
from file_operation import *
import os
import time
import re

def randomly_make_cifs_from_annxyz(): 

    input_dic = parse_input_file('input.json')

    mkdir('cif_coll')


    set_cutoff = input_dic['set_cutoff']
    atoms_step = read('ann.xyz',index=":")

    #1
    N_cif_chosen = input_dic['N_cif_chosen']
    N_step = len(atoms_step)
    N_chosen_4_each_step = int(N_cif_chosen/N_step)
    
    if N_chosen_4_each_step == 0:
      N_chosen_4_each_step = 1
      steps = random.sample(range(N_step),N_cif_chosen)
    else:
      steps = range(N_step)
        

    count = -1
    for step in steps:

        count += 1
        #mkdir('cif_coll/'+str(step).zfill(5))

        atoms = atoms_step[step]

        natm = len(atoms)

        atm_ids_pool = list(np.arange(natm))

        #print("atm_ids_pool=",atm_ids_pool)
        #print("N_chosen_4_each_step=",N_chosen_4_each_step)
        if natm > N_chosen_4_each_step:
            atm_ids_chosen = random.sample(atm_ids_pool, N_chosen_4_each_step)
        else:
            atm_ids_chosen = atm_ids_pool
        #print("atm_ids_chosen=",atm_ids_chosen)
        
        for atm_id in atm_ids_chosen:
            atoms_nl=gen_atoms_for_a_given_atm_id(atoms,atm_id, set_cutoff)
            atoms_nl.center()
            atoms_nl_minbox=smallest_cell_make(atoms_nl)

            write('cif_coll/'+str(count).zfill(4)+'.step_'+str(step).zfill(5)+'.atmid_'+str(atm_id).zfill(5)+'.cif',atoms_nl_minbox)


if __name__ == "__main__":

    randomly_make_cifs_from_annxyz()
