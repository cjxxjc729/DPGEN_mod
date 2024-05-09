#!/home/cjx/deepmd-kit-2.2.9/bin/python

import sys

import numpy as np
import os
import time
import re
import shutil
import json


def read_json(filename):
    '''
    normally read json
    '''

    with open(filename, 'r') as file:
      json_data = json.load(file)

    return json_data


def write_json(filename, json_data):
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=4)


def current_iter_judge():
    
    home_dir = os.getcwd()

    iter_idx_p1 = home_dir.split("/iter")[-1]

    if '/' in iter_idx_p1:
        iter_idx = iter_idx_p1.split('/')[0]
    else:
        iter_idx = iter_idx_p1

    current_iter = 'iter'+iter_idx
    last_iter = 'iter'+str(int(iter_idx)-1).zfill(2)

    return current_iter, last_iter



def copy_folder(src_folder, dst_dir=None):
    """
    将指定的文件夹复制到目标目录。
    如果目标目录中存在同名文件夹，则先删除它。

    参数:
    src_folder: 要复制的源文件夹路径。
    dst_dir: 目标目录路径。如果为None，则使用当前工作目录。
    """
    # 获取源文件夹的基本名称（即最后一个路径组件）
    folder_name = os.path.basename(src_folder)
    
    # 如果未指定目标目录，则使用当前工作目录
    if dst_dir is None:
        dst_dir = os.getcwd()
    
    # 构建目标文件夹的完整路径
    dst_folder = os.path.join(dst_dir, folder_name)
    
    # 检查目标文件夹是否已存在
    if os.path.exists(dst_folder):
        # 存在，则删除
        shutil.rmtree(dst_folder)
        print(f"已删除 {dst_folder}")
    
    # 复制源文件夹到目标位置
    shutil.copytree(src_folder, dst_folder)
    print(f"已将 {src_folder} 复制到 {dst_dir}")


def rename_file_or_directory(old_name, new_name):
    """
    Rename a file or directory from old_name to new_name. If new_name already exists,
    it is deleted before the renaming operation.
    
    Parameters:
    - old_name (str): The current name of the file or directory.
    - new_name (str): The new name you want to give to the file or directory.
    
    Returns:
    - bool: True if the rename operation was successful, False otherwise.
    """
    try:
        # Check if the new_name already exists
        if os.path.exists(new_name):
            # If it's a file, use os.remove(). If it's a directory, use shutil.rmtree().
            if os.path.isfile(new_name):
                os.remove(new_name)
                print(f"File '{new_name}' has been removed.")
            else:
                shutil.rmtree(new_name)
                print(f"Directory '{new_name}' has been removed.")
        
        # Now, rename old_name to new_name
        os.rename(old_name, new_name)
        print(f"'{old_name}' has been renamed to '{new_name}'.")
        return True
    except Exception as e:
        print(f"Error renaming/removing: {e}")
        return False
 

def mkdir(path):
  if os.path.exists(path):
    shutil.rmtree(path)
  os.makedirs(path, exist_ok=True)


def mkdir_if_not_exists(directory_path):

  if not os.path.exists(directory_path):
    os.makedirs(directory_path)
  else:
    print(f"Directory {directory_path} already exists.")


def parse_input_file_normal(filename):
    '''
    normally read json
    '''
     
    with open(filename, 'r') as file:
      json_data = json.load(file)

    return json_data


def convert_to_abs_path_in_f_json(filename):

    with open(filename, 'r') as file:
      json_data = json.load(file)

    convert_paths_to_absolute(json_data)

    with open(filename, 'w') as file:
      json.dump(json_data, file, indent=4)


def parse_input_file(filename):
   
    with open(filename, 'r') as file:
      json_data = json.load(file)

    convert_paths_to_absolute(json_data)

    with open(filename, 'w') as file:
      json.dump(json_data, file, indent=4)

    results = extract_values_with_parent_keys(json_data)
  
    return results


def convert_paths_to_absolute(obj):
    if isinstance(obj, dict):
        for key, value in list(obj.items()):
            if isinstance(value, dict) or isinstance(value, list):
                convert_paths_to_absolute(value)
            else:
                if isinstance(value, str) and '/' in value:
                    obj[key] = os.path.abspath(value)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            if isinstance(item, dict) or isinstance(item, list):
                convert_paths_to_absolute(item)
            else:
                if isinstance(item, str) and '/' in item:
                    obj[i] = os.path.abspath(item)


def extract_values_with_parent_keys(obj, parent_key='', result=None):
    if result is None:
        result = {}

    if isinstance(obj, dict):
        for key, value in obj.items():
            # 如果值是字典，继续递归，但不更新结果
            if isinstance(value, dict):
                extract_values_with_parent_keys(value, key, result)
            elif isinstance(value, list):
                # 对于列表，我们遍历每个元素，但传递当前的key作为父key
                for item in value:
                    extract_values_with_parent_keys(item, key, result)
            else:
                #相对路径转绝对路径
                #if isinstance(value, str) and '/' in value:
                #    value = os.path.abspath(value)
                # 对于非字典和列表的值，直接使用父key作为结果字典的key
                result[key] = value
    elif isinstance(obj, list):
        # 如果直接就是列表，对每个元素递归调用本函数
        for item in obj:
            extract_values_with_parent_keys(item, parent_key, result)

    return result





if __name__ == "__main__":

  f_input = 'input.json'

  variables = parse_input_file(f_input)

  print(variables)

  
  
