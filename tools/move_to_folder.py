import argparse
import os


# 使用说明：
# python move_to_folder.py --source_path Z:\JableTV\Jable\yua-mikami --destination_path Z:\videos\yua-mikami
def get_parser():
    parser = argparse.ArgumentParser(description="Jable move to folder")
    parser.add_argument("--source_path", type=str, default=r"C:\Users\Downloads",
                        help="源目录")
    parser.add_argument("--destination_path", type=str, default=".\\",
                        help="想要保存到的目录")

    return parser


parser = get_parser()
args = parser.parse_args()

source_path = args.source_path
destination_path = args.destination_path

# 1 获取原目录下所有文件的文件名
file_names = os.listdir(source_path)

videos = []
for name in file_names:
    if (name.endswith(".mp4")):
        videos.append(name)
# 2 将mp4文件转移至目标目录
for video_name in videos:
    prefix = os.path.splitext(video_name)[0]
    source_file = os.path.join(source_path, video_name)
    destination_file = os.path.join(os.path.join(destination_path, prefix), video_name)
    destination_real_path = os.path.join(destination_path, prefix)
    if not os.path.exists(destination_real_path):
        os.makedirs(destination_real_path)
    os.rename(source_file, destination_file)
# 3 如果目标目录下存在对应名字的文件夹，则将jpg文件转移到目标目录对应名字的文件夹下
for name in file_names:
    if (name.endswith(".jpg")):
        prefix = os.path.splitext(name)[0]
        source_file = os.path.join(source_path, name)
        destination_file = os.path.join(os.path.join(destination_path, prefix), name)
        destination_real_path = os.path.join(destination_path, prefix)
        if os.path.exists(destination_real_path):
            os.rename(source_file, destination_file)
