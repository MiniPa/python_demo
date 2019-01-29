# 利用命名空间解析 XML 文档

## 解析这个文档并执行普通查询，步骤变得相当繁琐

from xml.etree.ElementTree import parse, Element

doc = parse('6.07 eg.xml')

doc.findtext('author') # 'David Beazley'
doc.find('content')
doc.find('content/html')
doc.find('content/{http://www.w3.org/1999/xhtml}html')
# <Element '{http://www.w3.org/1999/xhtml}html' at 0x1007767e0>

## 将命名空间处理逻辑包装为一个工具类来简化这个过程
class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)
    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'
    def __call__(self, path):
        return path.format_map(self.namespaces)

ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
doc.find(ns('content/{html}html')) # <Element '{http://www.w3.org/1999/xhtml}html' at 0x1007767e0>
doc.findtext(ns('content/{html}html/{html}head/{html}title')) # 'Hello World'

## 基本的 ElementTree 解析中没有任何途径获取命名空间的信息
#  使用 iterparse() 函数的话就可以获取更多关于命名空间处理范围的信息

from xml.etree.ElementTree import iterparse

for evt, elem in iterparse('ns2.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)
# end <Element 'author' at 0x10110de10>
# start-ns ('', 'http://www.w3.org/1999/xhtml')
# end <Element '{http://www.w3.org/1999/xhtml}title' at 0x1011131b0>
# end <Element '{http://www.w3.org/1999/xhtml}head' at 0x1011130a8>
# end <Element '{http://www.w3.org/1999/xhtml}h1' at 0x101113310>
# end <Element '{http://www.w3.org/1999/xhtml}body' at 0x101113260>
# end <Element '{http://www.w3.org/1999/xhtml}html' at 0x10110df70>
# end-ns None
# end <Element 'content' at 0x10110de68>
# end <Element 'top' at 0x10110dd60>
print(elem) # <Element 'top' at 0x10110dd60>

## 如果要处理的 XML 文本，除了要使用到其他高级 XML 特性外，还要用到命名空间，建议最好使用 lxml 代替 ElementTree
#  例 lxml 利用对 DTD 文档验证，更好的 XPath 支持和一些其他高级 XML 特性，提供了更好的支持
































