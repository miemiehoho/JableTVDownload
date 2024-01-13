# author: hcjohn463
# !/usr/bin/env python
# coding: utf-8
import os

from args import *
from download import download
from download_threadpool import download_threadpool
from makedir import makedirs
from movies import movieLinks

# In[2]:

parser = get_parser()
args = parser.parse_args()

encode = args.encode
workers = args.workers
actorName = args.actor_name
output_dir = os.path.join(args.output, actorName)
temp_dir = os.path.join(os.path.join(os.getcwd(), 'temp'), actorName)
# 创建目录
makedirs(temp_dir, output_dir)

if (len(args.url) != 0):
    url = args.url
    download(url, encode, temp_dir, output_dir)
elif (args.random == True):
    url = av_recommand()
    download(url, encode, temp_dir, output_dir)
elif (args.all_urls != ""):
    all_urls = args.all_urls
    urls = movieLinks(all_urls)
    # 多线程下载
    download_threadpool(urls, encode, temp_dir, output_dir, workers)
else:
    # 使用者輸入Jable網址
    url = input('輸入jable網址,默认不转档:')
    download(url, encode, temp_dir, output_dir)
