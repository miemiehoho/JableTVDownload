import os


def makedirs(temp_dir, output_dir):
    # 创建临时目录
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    os.chdir(temp_dir)
    print("临时目录 " + os.getcwd())
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    os.chdir(output_dir)
    print("输出目录 " + os.getcwd())


def make_film_dirs(file_temp_dir, file_output_dir):
    # 创建临时目录
    if not os.path.exists(file_temp_dir):
        os.makedirs(file_temp_dir)
    os.chdir(file_temp_dir)
    print("影片临时目录 " + os.getcwd())
    # 创建输出目录
    if not os.path.exists(file_output_dir):
        os.makedirs(file_output_dir)
    os.chdir(file_output_dir)
    print("影片输出目录 " + os.getcwd())
