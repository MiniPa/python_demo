# 接受任意数量参数的函数

print('=========1=========')
def avg(first, *rest):
    '''
    接受任意数量位置参数
    :param first:
    :param rest:
    :return:
    '''
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 5))
print(avg(1, 2, 3, 4))

print('=========2=========')
import html

def make_element(name, value, **attrs):
    '''
    接受任意数量的关键字参数，使用一个以 ** 开头的参数
    :param name:
    :param value:
    :param attrs: 一个包含所有被传入进来的关键字参数的字典
    :return:
    '''
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element

# Creates '<item size="large" quantity="6">Albatross</item>'
ele1 = make_element('item', 'Albatross', size='large', quantity=6)
print(ele1)

# Creates '<p>&lt;spam&gt;</p>'
ele2 = make_element('p', '<spam>')
print(ele2)

print('=========3=========')
## 同时接收任意数量的 位置参数 和 关键字参数，可以同时使用 *和**
def anyargs(*args, **kwargs):
    print(args) # A tuple
    print(kwargs) # A dict

#  * 参数只能出现在函数定义中最后一个位置参数后面
#  ** 参数只能是最后一个参数
#  在 * 参数后面仍然可以定义其他参数

def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass






























