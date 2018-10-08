# CREATED FOR TEST 1

import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.dili360.com/'

ht = requests.get(url)
ht.encoding = ht.apparent_encoding
htt = ht.text
htts = BeautifulSoup(htt, "lxml")
img_tag = htts.find_all('img')
for i in img_tag:
    # print(i)
    if len(i.attrs) == 2:
        for n in i.attrs:
            if 'http' in i.attrs[n]:
                print(i.attrs[n])
    else:
        s = str(i)
        if 'jpg' in s:
            src = re.findall(r'http(.*)\.jpg', s)
            if src:
                print('http' + src[0] + '.jpg')
        if 'png' in s:
            src = re.findall(r'http(.*)\.png', s)
            if src:
                print('http' + src[0] + '.png')
        if 'gif' in s:
            src = re.findall(r'http(.*)\.gif', s)
            if src:
                print('http' + src[0] + '.gif')
