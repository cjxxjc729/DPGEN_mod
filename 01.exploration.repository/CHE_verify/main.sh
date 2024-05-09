#!/bin/bash
home_dir=$(pwd)
signature=$0
#script_dir=
#tmp_dir=
#mkdir 

#read -p "enter the prefix: " prefix
#read -p "enter the ref pwin file: " f_ref

#--------------------------------------------------------

fs_xyz=$(lxargs xyz)

for f_xyz in $fs_xyz
do
    prefix=$(echo $f_xyz | awk -F '_final.xyz' '{print $1}')
    #cp -r CAT0 ${prefix} 
    cp $f_xyz $prefix/blank.xyz

done
