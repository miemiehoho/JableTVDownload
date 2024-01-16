# In[0]:
# 相关模块导入
import time

from bs4 import BeautifulSoup
from selenium import webdriver


# 使用
# python movies_url.py
# momonogi-kana
# https://jable.tv/models/momonogi-kana/,https://jable.tv/models/momonogi-kana/2/

def movies_url(url, actor_name, num):
    links = []
    dr = webdriver.Chrome()
    dr.minimize_window()
    dr.get(url)
    # 设置3秒的等待时长
    time.sleep(3)
    bs = BeautifulSoup(dr.page_source, "html.parser")
    a_tags = bs.select('div.img-box>a')
    print(a_tags)
    for a_tag in a_tags:
        links.append(a_tag['href'])
    print('获取到 {0} 個影片'.format(len(links)))

    # 写入url
    writer = open(actor_name + "-urls.txt", "a")
    for link in links:
        writer.write(link + "\n")
    # 关闭打开的文件
    writer.close()
    writer = open(actor_name + "-" + str(num) + "-urls.txt", "a")
    for link in links:
        writer.write(link + "\n")
    writer.close()


if __name__ == '__main__':
    actor_name = input("请输入演员名：")
    var_num = 1
    url_list = input("请輸入多个jable網址，用逗号分隔")
    urls = url_list.split(",")
    num = 1
    for url in urls:
        print("参数：" + url + " " + actor_name + " " + str(num))
        movies_url(url, actor_name, num)
        num = num + 1
