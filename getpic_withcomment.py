import requests
from bs4 import BeautifulSoup
import re  # re 用于匹配网址http

url = 'http://www.dili360.com/'
# 国家地理网站

ht = requests.get(url)
ht.encoding = ht.apparent_encoding
# 解析全部代码的编码形式，给出实际的代码编码格式
htt = ht.text
htts = BeautifulSoup(htt, "lxml")
img_tag = htts.find_all('img')
# 'lxm'和'html.parser'解析出的是相同的img_tag
m = 0
# 标记文件名

for i in img_tag:
	if len(i.attrs) == 2:
		# 有的标签内有两个源文件地址
		for n in i.attrs:
			if 'http' in i.attrs[n]:
				# 有的属性值并不是网址，此项挑出网址的属性值
				if 'jpg' in i.attrs[n]:
					with open(r'C:\Users\chunliu\Desktop\pic\%s.jpg' % str(m), 'wb') as f:
						f.write(requests.get(i.attrs[n]).content)
						# 记得加 .content 因为是二进制文件图片等
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
		# 接下来是只有一个属性的标签
		s = str(i)
		if 'jpg' in s:
			src = re.findall(r'http(.*)\.jpg', s)
			# 通过正则来匹配出网址，注意正则的用法
			if src:
				with open(r'C:\Users\chunliu\Desktop\pic\%s.jpg' % str(m), 'wb') as f:
					f.write(requests.get('http' + src[0] + '.jpg').content)
					# 正则使用注意，补全网址，用于获取文件
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

