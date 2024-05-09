#!/bin/bash
home_dir=$(pwd)
signature=$0
#script_dir=

'''
#for all the step #1, #2, #3 should be the same
'''
#1
#current_iter_num=$(pwd | awk -F 'iter' '{print $NF}' | awk -F '/' '{print $1}' )
#last_iter_num=$(echo "${current_iter_num}-1" | bc -l | awk {printf'("%02d\n",$0)'} )
#echo "current_iter_num is $current_iter_num"
#echo "last iter number is $last_iter_num"

#2 link
#connect_to_group_dp.no_input.sh ../../../iter$last_iter_num/04.training/training.main/

#3 initialize traj_coll

if [ -d ../traj_coll ]
then
    rm -r ../traj_coll
fi

mkdir ../traj_coll

#----------------------------------------------------------------------------------#
#4 main


./main.py > log 

#holdon_v1

#cp collect_all_trajs_to_annxyz.py ../traj_coll/

#cd ../traj_coll

#    ./collect_all_trajs_to_annxyz.py


fs_annxyz=$(find ./ -name ann.xyz | xargs )
count=0
for f_annxyz in $fs_annxyz
do
    ((count=count+1))
    if [ $count -eq 1 ]
    then
        cp  $f_annxyz ../traj_coll/
    else
        cat $f_annxyz >> ../traj_coll/ann.xyz
    fi
done


