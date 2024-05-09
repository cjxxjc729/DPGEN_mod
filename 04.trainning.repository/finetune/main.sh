#!/bin/bash
home_dir=$(pwd)
#script_dir=
#tmp_dir=
#mkdir 

#read -p "enter the prefix: " prefix
#read -p "enter the ref pwin file: " f_ref

#--------------------------------------------------------
make_dp_in_group.dpa1_finetune.sh << EOF
../../../
EOF

#twotime_ndeepmd=$(grep deepmd init/input-1.json | wc -l)
#if [[ ${twotime_ndeepmd} -gt 10000 ]]
#then
#  echo "adjust stop_batch to 100000"
#  sed -i 's/\("stop_batch":\s*\)[0-9]\+/\1100000/' init/input-1.json
#fi

./switch_numstep.py

cd init
./dp_sub_cjx.sh

cd ../
holdon_wait_following_dir_done_V2.sh 000 001 002 003 
