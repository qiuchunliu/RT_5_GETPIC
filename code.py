# CREATED FOR TEST
import requests
from bs4 import BeautifulSoup

url = 'https://www.sina.com.cn/'
ht = requests.get(url)
ht.encoding = 'utf-8'
html = ht.text
htmls = BeautifulSoup(html, 'html.parser')
img = htmls.find_all('img')
n = 0
for i in img:
    img_url = i.attrs['src']
    img = requests.get('http:' + img_url).content
    if 'jpg' in img_url:
        with open(r'C:\Users\chunliu\Desktop\qw\%s.jpg' % str(n), 'wb') as f:
            f.write(img)
    else:
        with open(r'C:\Users\chunliu\Desktop\qw\%s.gif' % (str(n)+'g'), 'wb') as f:
            f.write(img)
    n += 1
    # print(i.attrs['src'])
