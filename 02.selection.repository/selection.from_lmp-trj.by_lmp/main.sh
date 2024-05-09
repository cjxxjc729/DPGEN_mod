#!/bin/bash
home_dir=$(pwd)
signature=$0
#script_dir=
#tmp_dir=
#mkdir 

#read -p "enter the prefix: " prefix
#read -p "enter the ref pwin file: " f_ref

#--------------------------------------------------------
while [ ! -f ann.lammpstrj ]; do
    sleep 1 # 等待1秒，避免无限快速循环
done

echo "文件 'ann.lammpstrj' 已找到，退出循环。"
#-------------------------------------------------------

echo "[$signature ]: prepare the files: "

f_lpj=$(ls -1 | grep "lammpstrj$" | tail -1)


cp ../01.training/000/input.json ./
connect_to_group_dp.sh << EOF
../01.training/
EOF

ele_list=$(get_elelist_from_inpujason.py)


lpj-trj_dev_probe.by_lmp.sh << EOF
$f_lpj
${ele_list}
30
EOF

cd dev_xyz_collection
collect_labset_4_all_stdxyz.sh
