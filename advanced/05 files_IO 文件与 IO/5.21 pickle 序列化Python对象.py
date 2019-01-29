# 序列化 Python 对象
## 将一个 Python 对象序列化为一个字节流

import pickle

data = {'ele1':'ele1_content'} # Some Python object

print('=========1=========')
# f = open('5.21 somefile', 'wb')
# pickle.dump(data, f) ## 将一个对象序列化到文件
#
# f2 = open('5.21 somefile', 'rb')
# data2 = pickle.load(f2) # restore from a file
# print(data2)


print('=========2=========')
# serial_str = pickle.dumps(data) ## 将一个对象变字符串
# print(serial_str)
#
# s2 = pickle.loads(serial_str)
# print(s2)


print('=========3=========')
## pickle 是一种 Python 特有的自描述的数据编码
#  通过自描述，被序列化后的数据包含每个对象开始和结束以及它的类型信息

f = open('5.21-2 somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()

f = open('5.21-2 somedata', 'rb')
data1 = pickle.load(f)
data2 = pickle.load(f)
data3 = pickle.load(f)
print(data1, data2, data3)

print('=========4=========')
## 还可以序列化函数、类、接口，但结果数据仅仅将它们的名称编码成对应的对象

import math
import pickle
serial_cos = pickle.dumps(math.cos)
print(serial_cos)

# 当数据反序列化回来的时候，会先假定所有的源数据是可用的，模块、类、函数会自动按需导入进来
# Python数据被不同机器上的解析器所共享的应用程序而言，数据的保存可能会有问题，所有的机器必须访问同一个源代码
# note: 不要对不信任的数据使用 pickle.load(), pickle 在加载时候副作用是自动加载相应的模块，并构造实例对象
#       一定要保证pickle只在互相之间可以认证对方解析器的内部使用

# 有些类型的对象不能被序列化，通常是哪些依赖外部系统状态的对象，如打开的文件、网络连接、线程、进程、栈帧等等
# 用户自定义类可以通过 __getstate__()、__setstate__() 方法来绕过这些限制
# 如果定义了这两个方法、pickle.dump() 就会调用 __getstate__() 获取序列化的对象，反序列化同理

print('=========5=========')
## 如下是一个内部定义了一个线程、但仍然可以序列化和反序列化的类 见 5.21CountDown.py

# countdown.py
import time
import threading

class CountDown:

    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(1)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)

c = CountDown(5)
c.run()
print(c)

# After a few moments
f = open('cstate.p', 'wb')
pickle.dump(c, f)
f.close()

# 然后退出 Python 解析器并重启后再试验下：
f = open('cstate.p', 'rb')
pickle.load(f)
# 线程会在你序列化它的地方又恢复了过来

## 1.pickle 对于大型的数据结构比如 array 或 numpy 模块创建的二进制数组效率并不是一个高效的编码方式。
# 如需移动大量的数组数据、最好现在一个文件中将其保存为数组数据块或使用更高级的编码方式如 HDF5(需第三方库支持)

## 2.pickle 是 Python 特有的并且附着在源码上，如需长期存储数据的时候，不应该选用它。
# 如源码变动了，所有的存储数据可能会被破坏并且变得不可读取
# 在数据库和存档文件中存储数据时，最好使用更加标准的数据格式如 XML、CSV、JSON

## pickle 有大量的配置选项和一些棘手问题，对于最常见的使用场景、多查官方文档
# https://docs.python.org/3/library/pickle.html







































