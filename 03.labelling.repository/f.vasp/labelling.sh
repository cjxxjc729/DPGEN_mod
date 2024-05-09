#!/bin/bash
home_dir=$(pwd)
#script_dir=
#tmp_dir=
#mkdir 

#read -p "enter the prefix: " prefix
#read -p "enter the ref pwin file: " f_ref


#--------------------------------------------------------


#before doing it, use extract_cif_v2.py to get the fs_cif_coll floder
mv ../../02.selection/selection.main/cif_coll fs_cif_coll
cd fs_cif_coll
#fs_cif=$(lxargs cif)
#cif_to_vaspin_with_fix_list.sh << EOF
#$fs_cif
#EOF

  echo "all_cif_to_vaspin_with_fix_list.scf.sub.sh"
  all_cif_to_vaspin_with_fix_list.scf.sub.sh >> /dev/null
  echo "sleep 30s"
  sleep 30s
  holdon_wait_following_dir_done_V2.sh
  uniorder_fids.hpc_multi.sh << EOF
10
make_deepmd_files.py;cd deepmd;raw_to_set.sh 50
EOF
  holdon

  filter_deepmd_4_subdirs_by_force.sh

  check_deepmd_4_subdirs.sh << EOF
yes
EOF

  pack_deepmd_and_del_cifvasp.sh

