# 将字典转换为XML

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

print('=========1=========')
def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)
print(e) # <Element 'stock' at 0x1004b64c8>
print(tostring(e)) # b'<stock><name>GOOG</name><shares>100</shares><price>490.1</price></stock>'

e.set('_id', '1234')
print(tostring(e)) # b'<stock _id="1234"><name>GOOG</name><shares>100</shares><price>490.1</price></stock>'

print('=========2=========')
## 创建XML的时候，被限制只能构造字符串类型的值
def dict_to_xml_str(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key,val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)

## 手动构造 遇到一些特殊字符时候，就比较麻烦
d = { 'name' : '<spam>' }

dict_to_xml_str('item',d) # '<item><name><spam></name></item>'
e = dict_to_xml('item',d)
print(tostring(e)) # b'<item><name>&lt;spam&gt;</name></item>'
# 字符‘<’和‘>’被替换成了 &lt; 和 &gt
# 手动转换  xml.sax.saxutils 中的 escape() 和 unescape() 函数

from xml.sax.saxutils import escape, unescape

spam = escape('<spam>')
print(spam)
print(unescape(spam))



















