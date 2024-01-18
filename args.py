import argparse
import random
import re
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def get_parser():
    parser = argparse.ArgumentParser(description="Jable TV Downloader")
    parser.add_argument("--random", type=bool, default=False,
                        help="Enter True for download random ")
    parser.add_argument("--url", type=str, default="",
                        help="Jable TV URL to download")
    parser.add_argument("--all-urls", type=str, default="",
                        help="Jable URL contains multiple avs")
    parser.add_argument("--actor-name", type=str, default="other",
                        help="Actor Name")
    parser.add_argument("--encode", type=str, default="0",
                        help="0不转档 1GPU转档  2CPU转档")
    parser.add_argument("--output", type=str, default="output",
                        help="输出路径")
    parser.add_argument("--workers", type=int, default="1",
                        help="工作线程数量")
    parser.add_argument("--urls_path", type=str, default="",
                        help="url文件路径")

    
    return parser


def av_recommand():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://jable.tv/'
    request = Request(url, headers=headers)
    web_content = urlopen(request).read()
    # 得到繞過轉址後的 html
    soup = BeautifulSoup(web_content, 'html.parser')
    h6_tags = soup.find_all('h6', class_='title')
    av_list = re.findall(r'https[^"]+', str(h6_tags))
    return random.choice(av_list)


# print(av_recommand())
