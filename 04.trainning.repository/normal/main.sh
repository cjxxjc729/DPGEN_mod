#!/bin/bash
home_dir=$(pwd)
#script_dir=
#tmp_dir=
#mkdir 

#read -p "enter the prefix: " prefix
#read -p "enter the ref pwin file: " f_ref

#--------------------------------------------------------

make_dp_in_group.sh << EOF
../../../
EOF

./switch_numstep.py

cd init
./dp_sub_cjx.sh

cd ../
holdon_wait_following_dir_done_V2.sh 000 001 002 003 
