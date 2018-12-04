# 实现一个优先级队列, 并且pop总返回优先级最高的元素
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0 # 保证同优先级的元素,按插入的顺序排序

    def push(self, item, priority):
        # -priority 优先级为负数目的是使得函数按照优先级从高到低排序，默认是由低到高
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('D'), 4)
q.push(Item('B2'), 2)
q.push(Item('B1'), 2)
q.push(Item('F'), 6)
q.push(Item('A'), 1)
q.push(Item('E'), 5)
q.push(Item('C'), 3)
print("PriorityQueue start ==>")
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

## push 和 pop 时间复杂度为O(logN), N为堆大小.

## index 涉及到排序支持问题，假设 Item实例不支持排序
print('====================')
a = Item('abc')
b = Item('bcd')
# print(a < b)  # Exception

print('====================')
a = (2, Item('abc'))
b = (3, Item('bcd'))
print(a < b)
c = (2, Item('cde'))
# print(a < c) # Exception

print('====================')
a = (1, 0, Item('abc'))
b = (5, 1, Item('bcd'))
a = (1, 2, Item('cde'))
print(a < b)
print(a < c)






