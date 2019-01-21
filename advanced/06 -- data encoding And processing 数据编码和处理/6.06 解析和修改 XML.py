# 解析和修改 XML

from xml.etree.ElementTree import parse, Element

doc = parse('6.06 pred.xml')
root = doc.getroot()
print(root)

root.remove(root.find('sri'))
root.remove(root.find('cr'))
index = root.getchildren().index(root.find('nm'))
print(index)

e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

doc.write('newpred.xml', xml_declaration=True)


## 所有的修改针对的都是父节点的元素，将它作为一个列表处理
#  索引操作是ok的，如 element[i] 或 element[i:j]





















