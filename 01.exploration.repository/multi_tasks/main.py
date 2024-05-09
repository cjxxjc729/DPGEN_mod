#!/home/cjx/deepmd-kit-2.2.9/bin/python

import sys
sys.path.append("../../functions")

import numpy as np
import os
import time
import re

import subprocess
import json
import time
import shutil


from file_operation import *
#from collect_all_trajs_to_annxyz import *
#from randomly_make_cifs_from_annxyz import *


def load_type(step_name, template_loc,type): 

    '''
    load type.
    use it when current dir is root dir of each step, list in 01.exploration
    '''


    dir_name = step_name.split(".")[1]+'.main'

    copy_folder(template_loc+'/'+type, step_name+'/')
    rename_file_or_directory(step_name+'/'+type, step_name+'/'+dir_name)


    return print(template_loc+'/'+type+' is loaded')


def adjust_inside_input(domain_input_dic,step_name='01.exploration'):
    '''
    adjust the inside input based on domain input
    '''

    dir_name = step_name.split('.')[1]+'.main'

    inside_f_input   = step_name+'/'+dir_name+'/'+'input.json'
    inside_input_dic = parse_input_file_normal(inside_f_input) 
    
    #3 domain_exploration_parameters_dic 是exploration当中的parameters
    domain_parameters_dic = domain_input_dic[step_name]['parameters']

    for key,value in domain_parameters_dic.items():

        print("key=",key)
        #用递归的方法修改内部inside_input_dic的值，以使其和外部的json保持一致
        modify_dict_values(inside_input_dic, key, value)
        with open(inside_f_input, "w") as f:
            json.dump(inside_input_dic, f, indent=4)

    return print(inside_f_input+" is adjusted")


def modify_dict_values(dic, target_key, new_value):
    """
    递归遍历字典，如果找到键等于target_key，则修改其值为new_value。

    :param d: 要遍历的字典。
    :param target_key: 目标键，如果找到，将修改其值。
    :param new_value: 新的值，用于替换目标键的值。
    :return: None，直接在原字典上修改。
    """
 

    for key in list(dic.keys()):
        if isinstance(dic[key], dict):  # 如果值是字典，则递归调用
            modify_dict_values(dic[key], target_key, new_value)
        elif key == target_key:  # 如果找到目标键，则修改其值
            print("d[key] = new_value", dic[key], new_value)
            dic[key] = new_value
    

def run_step(step_name, iter01_mode=False):

    mkdir(step_name)

    #step 1 read domain input.json
    domain_f_input = 'input.json'
    domain_input_dic = parse_input_file_normal(domain_f_input)

    #step 2 read type and template_loc
    if iter01_mode:
        type = domain_input_dic[step_name]['type_iter01']
    else:
        type = domain_input_dic[step_name]['type']

    template_loc = domain_input_dic[step_name]['template_loc']

    #step3
    #prepare the *.main and its inside input.json
    load_type(step_name, template_loc, type)  #will copy type fid here
    adjust_inside_input(domain_input_dic,step_name)  #will adjudt inside input.json  
    
    #step4.run
    home_dir = os.getcwd()
    dir_name = step_name.split('.')[1]+'.main'

    os.chdir(step_name+'/'+dir_name+'/')
    
    command = ["./main.sh"]

    print("\n",step_name ,": shell command =", command,"\n")

    with open('a.out','w') as output_file:
        subprocess.run(command, text=True, stdout=output_file, stderr=subprocess.PIPE)

    #send end signal
    os.chdir(home_dir)
    subprocess.run(["touch", step_name+"/"+"end.signal"])


    #iter_name = home_dir.split('/')[-1]
    
    #rint("randomly pick")
    #s.chdir('02.selec')    
    #randomly_make_cifs_from_annxyz()

    #subprocess.run(["touch", "end.signal"])
    #os.chdir(home_dir)


def parallelly_run_multi_step(jobs_index, iter01_mode=False):

    processes = []

    for job_idx in jobs_index:

        mkdir(job_idx)

        #step 1 read domain input.json
        domain_f_input = 'input.json'
        domain_input_dic = parse_input_file_normal(domain_f_input)

        #step 2 read type and template_loc
        if iter01_mode:
            type = domain_input_dic[job_idx]['type_iter01']
        else:
            type = domain_input_dic[job_idx]['type']

        template_loc = domain_input_dic[job_idx]['template_loc']

        #step3
        #prepare the *.main and its inside input.json
        load_type(job_idx, template_loc, type)  #will copy type fid here
        adjust_inside_input(domain_input_dic,job_idx)  #will adjudt inside input.json  

        #step4.run
        home_dir = os.getcwd()
        dir_name = job_idx.split('.')[1]+'.main'

        os.chdir(job_idx+'/'+dir_name+'/')

        command = ["./main.sh"]

        print("\n", job_idx,": shell command =", command,"\n")

        # 启动进程
        process = subprocess.Popen(['./main.sh'])

        # 将进程添加到列表中
        processes.append(process)

        os.chdir(home_dir)

    for process in processes:
        process.wait()



        #with open('a.out','w') as output_file:
            #subprocess.run(command, text=True, stdout=output_file, stderr=subprocess.PIPE)
            #process = subprocess.Popen(command, stdout=output_file, stderr=subprocess.PIPE, text=True)

    #send end signal
    #os.chdir(home_dir)
    #subprocess.run(["touch", step_name+"/"+"end.signal"])


  
if __name__ == "__main__":

    #1. env make

    convert_to_abs_path_in_f_json('input.json')

    json_data = read_json('input.json')

    n_parallel = 8
    #n_parallel = json_data['n_parallel']
    
    current_iter, last_iter = current_iter_judge()

    #2. main

    jobs_index = []

    count = 0
    nkey_tot = len(json_data.items())
    for key,value in json_data.items():
        count += 1

        job_idx = key

        print("job_idx=",job_idx)
        jobs_index.append(job_idx)

        #every time praellly sub 4 jobs
        if count % n_parallel == 0 or count == nkey_tot:
            parallelly_run_multi_step(jobs_index, iter01_mode = (current_iter == 'iter01'))
            jobs_index = [] 



