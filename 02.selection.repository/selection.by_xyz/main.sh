#!/bin/bash
home_dir=$(pwd)
signature=$0
#script_dir=
#tmp_dir=
#mkdir 

#read -p "enter the prefix: " prefix
#read -p "enter the ref pwin file: " f_ref

#--------------------------------------------------------
#while [ ! -f ann.lammpstrj ]; do
#    sleep 1 # 等待1秒，避免无限快速循环
#done
#
#echo "文件 'ann.lammpstrj' 已找到，退出循环。"
#-------------------------------------------------------

echo "[$signature ]: prepare the files: "
cp ../../01.exploration/traj_coll/ann.xyz ./

f_xyz=$(ls -1 | grep "xyz$" | tail -1)

#0
model_dev_high_bound=$(read_json.py input.json model_dev_high_bound)
model_dev_low_bound=$(read_json.py input.json model_dev_low_bound)
N_cif_chosen=$(read_json.py input.json N_cif_chosen)

#1
current_iter_num=$(pwd | awk -F 'iter' '{print $NF}' | awk -F '/' '{print $1}' )
last_iter_num=$(echo "${current_iter_num}-1" | bc -l | awk {printf'("%02d\n",$0)'} )
echo "current_iter_num is $current_iter_num"
echo "last iter number is $last_iter_num"

#2 link
connect_to_group_dp.no_input.sh ../../../iter$last_iter_num/04.training/training.main/

#cp ../01.training/000/input.json ./
#connect_to_group_dp.sh << EOF
#../01.training/
#EOF

ele_list=$(get_elelist_from_pb.py graph.000.pb)


xyz-trj_dev_probe.by_lmp.sh << EOF
$f_xyz
${ele_list}
30
EOF

cd dev_xyz_collection
    collect_labset_4_all_stdxyz.sh ${model_dev_low_bound} ${model_dev_high_bound} ${N_cif_chosen}
    mv cif_coll_shorten ../cif_coll

