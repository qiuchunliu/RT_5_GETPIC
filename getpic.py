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
m = 0
for i in img_tag:
    if len(i.attrs) == 2:
        for n in i.attrs:
            if 'http' in i.attrs[n]:
                if 'jpg' in i.attrs[n]:
                    with open(r'C:\Users\chunliu\Desktop\pic\%s.jpg' % str(m), 'wb') as f:
                        f.write(requests.get(i.attrs[n]).content)  # 记得加 .content
                    m += 1
                elif 'png' in i.attrs[n]:
                    with open(r'C:\Users\chunliu\Desktop\pic\%s.png' % str(m), 'wb') as f:
                        f.write(requests.get(i.attrs[n]).content)
                    m += 1
                elif 'gif' in i.attrs[n]:
                    with open(r'C:\Users\chunliu\Desktop\pic\%s.gif' % str(m), 'wb') as f:
                        f.write(requests.get(i.attrs[n]).content)
                    m += 1
    else:
        s = str(i)
        if 'jpg' in s:
            src = re.findall(r'http(.*)\.jpg', s)
            if src:
                with open(r'C:\Users\chunliu\Desktop\pic\%s.jpg' % str(m), 'wb') as f:
                    f.write(requests.get('http' + src[0] + '.jpg').content)
                m += 1
        if 'png' in s:
            src = re.findall(r'http(.*)\.png', s)
            if src:
                with open(r'C:\Users\chunliu\Desktop\pic\%s.png' % str(m), 'wb') as f:
                    f.write(requests.get('http' + src[0] + '.png').content)
                m += 1
        if 'gif' in s:
            src = re.findall(r'http(.*)\.gif', s)
            if src:
                with open(r'C:\Users\chunliu\Desktop\pic\%s.png' % str(m), 'wb') as f:
                    f.write(requests.get('http' + src[0] + '.gif').content)
                m += 1
