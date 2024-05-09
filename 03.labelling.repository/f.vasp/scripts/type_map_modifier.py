#!/home/cjx/deepmd-kit-2.2.9/bin/python

import os

def replace_f_with_cl(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'type_map.raw':
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                content = content.replace('F', 'Cl')
                with open(file_path, 'w') as f:
                    f.write(content)

# 使用当前目录作为起始点
replace_f_with_cl('.')

