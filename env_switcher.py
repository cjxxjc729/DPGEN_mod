#!/home/cjx/deepmd-kit-2.2.9/bin/python

import os

# 设置新的Python解释器位置和root_dir的值
py_dir = "/public1/home/sch0149/deepmd-kit-2.2.9/bin/python3.11"
root_dir = "/public1/home/sch0149/"

# 遍历当前目录及所有子目录
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                lines = f.readlines()

            # 修改文件的第一行
            if lines:
                lines[0] = f"#!{py_dir}\n"

            # 修改前十行中的sys.path.append(部分
            for i, line in enumerate(lines[:10]):
                if "sys.path.append(" in line and "/script" in line:
                    # 找到"/script"的位置
                    script_index = line.find("/script")
                    # 仅替换"/script"之前的部分为新的root_dir
                    start = line.find('("') + 2
                    lines[i] = line[:start] + root_dir + line[script_index:]

            # 重新写入文件
            with open(file_path, "w") as f:
                f.writelines(lines)

