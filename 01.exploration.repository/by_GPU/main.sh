#!/bin/bash
home_dir=$(pwd)
signature=$0
#script_dir=
#tmp_dir=
#mkdir 

#read -p "enter the prefix: " prefix
#read -p "enter the ref pwin file: " f_ref

#--------------------------------------------------------
sleep_time=$(read_json.py input.json sleep_time)

mkdir ../traj_coll
while [ ! -f ../traj_coll/ann.xyz ]
do
  echo "does not find ann.xyz"
  sleep ${sleep_time}s
  echo "wating for input ann.xyz"
done

echo "found ann.xyz ! goes on"
