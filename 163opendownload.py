import requests
import os
import re
import sys
from bs4 import BeautifulSoup


def getsourse(url, filename):
    res = requests.get(url)
    # print(res.encoding)
    if res.status_code == 200:
        html = res.text
        soup = BeautifulSoup(html, 'html.parser', from_encoding = res.encoding)
        items = soup.find_all('td', class_ = 'u-ctitle')
        urls = []
        for item in items:
            # print(str(item))
            pattern = re.compile(r'(\[.*\])\n.*<a href="(.*)">(.*)</a>')
            tmp = pattern.findall(str(item))
            urls.append([tmp[0][1], tmp[0][0]+tmp[0][2]])
        download(urls, filename)

# unique list
def unique(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst


def download(urls, filename):
    urls = unique(urls)
    num = len(urls)
    for i, url in enumerate(urls):
        print(i+1, '/', num)
        os.system('you-get -o '+filename+' -O '+ url[1]+' '+url[0])


if __name__ == '__main__':
    if len(sys.argv)!=3:
        print('useage: python 163opendownload.py foldername url')
    else:
        try:
            getsourse(sys.argv[2], sys.argv[1])
        except:
            print('error')
            print('useage: python 163opendownload.py foldername url')
            print(sys.argv)
        
# getsourse('http://open.163.com/special/opencourse/machinelearning.html', 'cs229')