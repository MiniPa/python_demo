# 一个自定义容器对象，包含列表、元组或其他可迭代对象，在这个容器对象上执行迭代操作

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        '''
        Python迭代协议需要__iter__() 返回一个实现了 __next__()方法的迭代器对象
        如果只是迭代遍历其他容器内容，无需担心底层怎样实现，只要传递迭代请求即可

        iter() 函数的使用简化了代码，iter(s)只是简单通过调用 s.__iter__()方法来返回对应的迭代器对象
        和len(s)会调用s.__len__()原理是一样的
        '''
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)








































