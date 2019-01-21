# 从一个简单的 XML 文档中提取数据

from urllib.request import urlopen
from  xml.etree.ElementTree import parse

print('=========1=========')
# Download the RSS feed and parse it
u = urlopen('http://www.stemcloud.cn/')
doc = parse(u)
print(doc)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    '''channel/item 搜索所有在 channel 元素下面的 item 元素'''
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
    print()

print(doc)
e = doc.find('channel/title')
print(e)
print(e.tag)
print(e.text)
print(e.get('some_attribute'))

## 另外可以考虑使用 lxml, 完全遵循XML标准,并且速度非常快，同事支持验证 XSTL 和 XPath 等特性









































