#!/home/cjx/deepmd-kit-2.2.9/bin/python

import sys
from ase.io import write
from ase.io import read
from ase import neighborlist
from ase import geometry
import numpy as np
#from mimic_functions import *
import os
import time
import re

from sklearn.decomposition import PCA
from typing import Tuple


def smallest_cell_make_v2(atoms):


    cors = atoms.positions

    origin, center, dimensions, box = find_bounding_box_with_margin(cors)
    print("box", box)

    atoms.translate(-origin)
    atoms.set_cell(box)

    return atoms


def find_bounding_box_with_margin(points: np.ndarray, vac_thickness: float = 2.2) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Find an optimally oriented bounding box for a set of 3D points using PCA, calculate the edge vectors (OA, OB, OC),
    compute the origin of the bounding box, and add a margin (vacuum thickness) to the box dimensions.

    Parameters:
    - points (np.ndarray): An array of 3D points of shape (N, 3).
    - vac_thickness (float): The thickness of the vacuum to add around the bounding box.

    Returns:
    - Tuple containing:
        - origin (np.ndarray): The origin of the bounding box.
        - center (np.ndarray): The center of the box.
        - dimensions (np.ndarray): Dimensions of the box.
        - oa (np.ndarray): Vector OA representing one edge of the box.
        - ob (np.ndarray): Vector OB representing the second edge of the box.
        - oc (np.ndarray): Vector OC representing the third edge of the box.
    """
    # Initialize PCA model, fit to points
    pca = PCA(n_components=3)
    pca.fit(points)

    # Transform points to PCA components space
    points_rotated = pca.transform(points)

    # Find the dimensions of the bounding box in the rotated space and add vacuum thickness
    min_values_rotated = points_rotated.min(axis=0) - vac_thickness
    max_values_rotated = points_rotated.max(axis=0) + vac_thickness
    dimensions = max_values_rotated - min_values_rotated

    # The center of the bounding box in the rotated space, adjusted for the vacuum
    center_rotated = (max_values_rotated + min_values_rotated) / 2

    # Calculate the real center of the bounding box in the original space
    center = pca.inverse_transform(center_rotated)

    # Calculate the origin of the bounding box, adjusted for the vacuum
    origin_rotated = min_values_rotated
    origin = pca.inverse_transform(origin_rotated)

    # The orientation vectors of the box are the PCA components scaled by the dimensions
    edges = pca.components_ * dimensions[:, np.newaxis]

    return origin, center, dimensions, edges


def find_traj_files(directory):
    """
    Find all '.traj' files within a directory and its subdirectories.

    Parameters:
    - directory (str): The root directory to search in.

    Returns:
    - list of str: A list containing the paths to all '.traj' files found.
    """
    traj_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.traj'):
                traj_files.append(os.path.join(root, file))

    return traj_files


def collect_all_trajs_to_annxyz():

    # Replace 'your_directory_path' with the path to the directory you want to search in
    directory_path = './'
    fs_traj = find_traj_files(directory_path)
    print("Found .traj files:", fs_traj)

    atoms_coll=[]
    for f_traj in fs_traj:

        atoms_step = read(f_traj,index=':')
        for step in range(len(atoms_step)):

            atoms = atoms_step[step]
            atoms.center()
            atoms.wrap()
            new_atoms = smallest_cell_make_v2(atoms)
  
            atoms_coll.append(new_atoms)

    write('ann.xyz',atoms_coll)


if __name__=="__main__":

    collect_all_trajs_to_annxyz()


