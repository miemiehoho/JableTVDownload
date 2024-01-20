import argparse


# 使用说明：
# python find_undownloaded_videos.py --video_path Z:\videos\saika-kawakita --urls_path Z:\JableTVDownload\tools\saika-kawakita-urls.txt --actor_name saika-kawakita
def get_parser():
    parser = argparse.ArgumentParser(description="Jable move to folder")
    parser.add_argument("--video_path", type=str, default=r"C:\Users\Downloads",
                        help="视频目录")
    parser.add_argument("--urls_path", type=str, default="",
                        help="url文件路径")
    parser.add_argument("--actor_name", type=str, default="other",
                        help="Actor Name")
    return parser


import os


def traverse_directory(path):
    video_names = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # print(os.path.join(root, file))
            if (file.endswith(".mp4")):
                fileSplit_type_a = file.split(' ')
                video_names.append(fileSplit_type_a[0])
                fileSplit_type_b = file.split('.')
                video_names.append(fileSplit_type_b[0])
    print(video_names)
    return video_names


parser = get_parser()
args = parser.parse_args()

video_path = args.video_path
urls_path = args.urls_path
actor_name = args.actor_name

# 1 调用函数，遍历指定目录及其子目录下的所有文件
video_names = traverse_directory(video_path)
url_names = []
url_not_find = []
urls = []
# 2 读取所有url
with open(urls_path, 'r') as file:
    urls = file.readlines()
print(urls)
for url in urls:
    url_name = url.split('/')[-2]
    url_exist = 0
    for video_name in video_names:
        # print("url_name.lower() "+url_name.lower())
        # print("video_name.lower() "+video_name.lower())
        if url_name.lower() == video_name.lower():
            url_exist = 1
    if url_exist == 0:
        url_not_find.append(url)

# 写入没有视频的url
writer = open(actor_name + "-not-find-urls.txt", "w")
for url in url_not_find:
    writer.write(url + "\n")
writer.close()
print("查找完成，没有找到的视频个数：" + str(len(url_not_find)))
