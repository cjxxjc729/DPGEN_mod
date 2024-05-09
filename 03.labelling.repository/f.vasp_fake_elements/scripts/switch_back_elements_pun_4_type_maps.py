#!/home/cjx/deepmd-kit-2.2.9/bin/python

import os
import json

def read_json(filename):
    with open(filename, 'r') as file:
      json_data = json.load(file)

    return json_data


def write_json(filename, json_data):
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=4)



def replace_in_file(file_path, original_text, replacement_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            # 替换条件：行去除空白后等于原文本
            if line.strip() == original_text:
                line = line.replace(original_text, replacement_text)
            file.write(line)

def traverse_and_replace(directory, target_file, original_text, replacement_text):
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name == target_file:
                file_path = os.path.join(root, name)
                replace_in_file(file_path, original_text, replacement_text)

# 调用函数：示例
directory_path = './' # 设置为你的目录路径
target_file = 'type_map.raw'

json_data = read_json('../input.json')


element_pun_from = json_data['element_pun_from']
element_pun_to = json_data['element_pun_to']

original_text = element_pun_to
replacement_text = element_pun_from

# 遍历并替换
traverse_and_replace(directory_path, target_file, original_text, replacement_text)

