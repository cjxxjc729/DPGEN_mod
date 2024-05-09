#!/bin/bash
home_dir=$(pwd)
signature=$0
#script_dir=
#tmp_dir=
#mkdir 

#read -p "enter the prefix: " prefix
#read -p "enter the ref pwin file: " f_ref

for fid in 01.exploration.repository 02.selection.repository 03.labelling.repository 04.trainning.repository
do

    home_dir1=$(pwd)
    cd $fid
        fids1=$(lld)
        home_dir2=$(pwd)
        for fid1 in $fids1
        do
            cd $fid1
                pwd > link
            cd $home_dir2
        done
        

    cd $home_dir1

done

