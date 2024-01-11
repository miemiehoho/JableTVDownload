# author: hcjohn463
# !/usr/bin/env python
# coding: utf-8
import os

from args import *
from download import download
from movies import movieLinks

# In[2]:

parser = get_parser()
args = parser.parse_args()

if (len(args.url) != 0):
    url = args.url
    encode = args.encode
    download(url, encode)
elif (args.random == True):
    url = av_recommand()
    encode = args.encode
    download(url, encode)
elif (args.all_urls != ""):
    all_urls = args.all_urls
    actorName = args.actor_name
    urls = movieLinks(all_urls)
    encode = args.encode
    if not os.path.exists(actorName):
        os.makedirs(actorName)
    os.chdir(actorName)
    for url in urls:
        download(url, encode)
else:
    # 使用者輸入Jable網址
    url = input('輸入jable網址,默认CPU转档:')
    download(url, 2)
