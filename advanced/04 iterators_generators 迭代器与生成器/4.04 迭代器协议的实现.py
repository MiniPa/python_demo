# 迭代器协议的实现
## 构建一个能支持迭代操作的自定义对象，并找到一个能实现迭代协议的简单方法

## 实现一个以深度优先方式遍历树形节点的生成器
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        '''
        先返回自己本身并迭代每一个子节点
        并通过子节点的 depth_first() 方法，使用 yield from 返回对应的元素
        '''
        yield self
        for c in self:
            yield from c.depth_first()

# Example
if __name__ == '__main__':
    print('=========1===========')
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)


## Python 迭代协议要求一个 __iter__() 返回一个特殊的迭代器对象，
#  这个迭代器对象实现了 __next__() 方法，并通过 StopIteration 异常标识迭代的完成
#  但通常实现会比较繁琐，下面方式演示如何使用一个关联迭代器重新实现 depth_first() 方法

class Node2:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)

class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            # Return myself if just started; create an iterator for children
            self._children_iter = iter(self._node)
            return self._node
        elif self._child_iter:
            # If processing a child, return its next item
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            # Advance to the next child and start its iteration
            self._child_iter = next(self._child_iter).depth_first()
            return next(self)

## DepthFirstIterator 和上面使用生成器的版本工作原理相似，但写起来很繁琐，
#  因为迭代处理器必须在迭代处理过程中，维护大量的状态信息

# Example
if __name__ == '__main__':
    print('=========2===========')
    root = Node2(0)
    child1 = Node2(1)
    child2 = Node2(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node2(3))
    child1.add_child(Node2(4))
    child2.add_child(Node2(5))

    for ch in root.depth_first():
        print(ch)




























