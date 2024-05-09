#!/bin/bash
home_dir=$(pwd)
signature=$0
#script_dir=
#tmp_dir=
#mkdir 

#read -p "enter the prefix: " prefix
#read -p "enter the ref pwin file: " f_ref

#--------------------------------------------------------

#n_cif=$(ls -1| grep cif$ | xargs)
job_names=$(ls -1 | grep blank.xyz$ | awk -F '.blank.xyz' '{print $1}' | xargs)


n_tot_to_do=$(ls -1  | grep fix_list | wc -l)
n_tot_done=$(ls -1  | grep log | wc -l)

while [[ ${n_tot_to_do} -ne ${n_tot_done} ]]
do
  for job_name in $job_names
  do
    echo "--- $job_name --------"

    n_to_do=$(ls -1 | grep ${job_name} | grep fix_list | wc -l)
    n_done=$(ls -1 | grep ${job_name} | grep log | wc -l)
    if [[ ${n_to_do} -ne ${n_done} ]] 
    then  
       job_num_control 
       hpc_sub_16Gmem "../opt_by_orr_jobname_opt.py $job_name"
    fi
  done
  echo "sleep 2m"
  sleep 2m
  holdon_v1

  n_tot_to_do=$(ls -1 | grep fix_list | wc -l)
  n_tot_done=$(ls -1 | grep log | wc -l)

done


