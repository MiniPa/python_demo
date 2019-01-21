# 用尽可能少的内存处理一个超大的XML文档

from xml.etree.ElementTree import iterparse

print('=========1=========')
def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

## 写一个脚本来按照坑洼报告数量排列邮编号码

from xml.etree.ElementTree import parse
from collections import Counter

print('=========2=========')
# 如下脚本加载整个XML文件，估计内存使用量 450M
potholes_by_zip = Counter()

doc = parse('potholes.xml')

for pothole in doc.iterfind('row/row'):
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)

print('=========3=========')
# 如下脚本只需约 7M 的内存
from collections import Counter

potholes_by_zip = Counter()

data = parse_and_remove('potholes.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)

## ElementTree
#  功能一：iterparse() 允许对XML文档进行增量操作，需提供文件名和一个包含下面一种或多种类型的事件列表：
#  start、end、start-ns、end-ns
#  iterparse()创建迭代器会生成形如 (event, elem)的元组, event 是上述事件列表中的一个、elem是相应的xml元素

data = iterparse('potholes.xml',('start','end'))
next(data) # ('start', <Element 'response' at 0x100771d60>)
next(data) # ('start', <Element 'row' at 0x100771e68>)

## start 事件在某个元素第一次被创建并且还没有被插入其他数据 (如子元素) 时被创建
## end 事件在某个元素已经完成时被创建
## start-ns 和 end-ns 事件被用来处理 XML 文档命名空间的声明

## start 和 end 事件被用来管理元素和标签栈
#  栈代表了文档被解 析时的层次结构，还被用来判断某个元素是否匹配传给函数 parse_and_remove() 的路径, 如果匹配，就利用 yield 语句向调用者返回这个元素

## 程序占用内存少的核心：elem_stack[-2].remove(elem)













































