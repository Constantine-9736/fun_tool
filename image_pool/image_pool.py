# -*- coding:utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
from memory_profiler import profile


@profile
def run():
    if not os.path.exists('./images/'):
        os.mkdir('./images/')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'
    for i in range(11):
        response = requests.get(url.format(i), headers=headers).text
        soup = BeautifulSoup(response, 'lxml')
        img_list = soup.find_all('img', class_='ui image lazy')
        for img in img_list:
            img_url = img['data-original']
            img_title = img['title']
            print(img_url, img_title)
            try:
                with open('./images/' + img_title + os.path.splitext(img_url)[-1], 'wb') as f:
                    image = requests.get(img_url, headers=headers).content
                    # 写入二进制数据 image这个变量是存储requests返回的二进制数据的
                    f.write(image)
                    print('保存成功:', img_title)
            except:
                pass


if __name__ == '__main__':
    run()
