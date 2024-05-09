#!/bin/bash
home_dir=$(pwd)
signature=$0
#script_dir=
#tmp_dir=
#mkdir 

#read -p "enter the prefix: " prefix
#read -p "enter the ref pwin file: " f_ref

#--------------------------------------------------------

if [ -d ../traj_coll ]
then
    rm -rf ../traj_coll
fi

mkdir ../traj_coll

./main.py

#holdon_v1

cp collect_all_trajs_to_annxyz.py ../traj_coll/

cd ../traj_coll

    ./collect_all_trajs_to_annxyz.py


