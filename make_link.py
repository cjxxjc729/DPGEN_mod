#!/home/cjx/deepmd-kit-2.2.9/bin/python

import os

def write_link_file_in_subdirs(parent_dir):
    # 遍历根目录下所有文件和文件夹
    for item in os.listdir(parent_dir):
        # 检查是否为以0开头的目录
        if item.startswith('0') and os.path.isdir(os.path.join(parent_dir, item)):
            subdir_path = os.path.join(parent_dir, item)
            # 遍历选中目录下的所有子目录
            for root, dirs, files in os.walk(subdir_path):
                for dir in dirs:
                    # 构建子目录的完整路径
                    dir_path = os.path.join(root, dir)
                    # 切换到该子目录
                    os.chdir(dir_path)
                    # 获取当前工作目录的路径
                    current_dir_path = os.getcwd()
                    # 创建（或覆盖）link文件，并写入当前工作目录的路径
                    with open("link", "w") as link_file:
                        link_file.write(current_dir_path)
                    print(f"link file written in {dir_path}")
            # 切回原来的工作目录，以便继续遍历
            os.chdir(parent_dir)

# 调用函数
root_directory = os.getcwd()  # 设置为你的根目录路径
write_link_file_in_subdirs(root_directory)

