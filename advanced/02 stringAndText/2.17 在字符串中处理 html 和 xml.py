# 在字符串中处理 html 和 xml
s = 'Elements are written as "<tag>text</tag>".'

## 转换文本中特定的字符 <、>等
import html
print('=========1=========')
print(s)
print(html.escape(s))
# Disable escaping of quotes
print(html.escape(s, quote=False))

## 正在处理ASCII文本，想将非ASCII文本对应的编码实体嵌入进去
## 可以给某些I/O函数传递参数 errors='xmlcharrefreplace' 达到这个目的
print('=========2=========')
s = 'Spicy Jalapeño'
s1 = s.encode('ascii', errors='xmlcharrefreplace')
print(s1)

## 若果接收到一些含有编码值的原始文本，需要手动替换，一般使用HTML或XML解析器的相关工具函数/方法即可
print('=========3=========')
s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
s2 = p.unescape(s)
print(s2)

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
t2 = unescape(t)
print(t2)

## 进行类似的处理，首先应该调研下怎样清楚的使用一个合适的解析器
## 如处理 HTML 或者 XML 文本，html.parse 或 xml.etree.ElementTree已经帮你自动处理了相关细节





