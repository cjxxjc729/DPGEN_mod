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

ln -s ../../../../functions/mimic_functions.py ./
ln -s ../../../../functions/file_operation.py ./

ln -s ../../01.exploration/traj_coll/ann.xyz ./

./modeldev_make_cifs_from_annxyz.py
