# 内联回调函数

# 当你编写使用回调函数的代码的时候，担心很多小函数的扩张可能会弄乱程序控制流
# 找到某个方法来让代码看上去更像是一个普通的执行序列

# 方案：通过使用生成器和协程可以使得回调函数内联在某个函数中

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)

print('=========1=========')
from queue import Queue
from functools import wraps

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper

print('=========2=========')
# 这两个代码片段允许你使用 yield 语句内联回调步骤

def add(x, y):
    return x + y

@inlined_async
def test():
    r = yield Async(add(2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')

## 除了特别的装饰器和yield外，其他地方并没有任何的回调函数（其实是在后台定义的）
## 回调函数、生成器、控制流的认识

#  1.回调：关键点在于当前工作会挂起来，并在将来某个时候重启（如异步执行），当计算重启时，回调函数被用来继续处理计算结果
#  apply_async() 演示了执行回调函数的实际逻辑，尽管实际情况中它可能更加复杂（包括线程、进程、事件处理器等）
#  2.生成器：yield 会使生成器函数产生一个值并暂停，调用__next()__ 或 send()又让它从暂停处继续执行
#  3.装饰器函数(核心)： inline_async() 装饰器会逐步遍历生成器函数所有的 yield 语句，每次一个。
#   刚开始创建了一个result队列并向里面放入了一个None值，然后开始一个循环操作，从队列中取出结果值并发送给生成器，它会持续到下一个 yield 语句
#   在这里一个Async的实例被接受到，然后开始循环开始检查函数和参数，并开始进行异步计算 apply_async()
#   这个计算最诡异的部分是它并没有使用一个普通的回调函数，而是用队列的 put() 方法来回调

#  4.实质：主循环立即返回顶部，并在队列上执行 get() 操作。
#   如果数据存在，它一定是 put() 回调存放的结果，如果没有数据，那么暂停操作并等待结果的到来，具体的实现是由 apply_async() 函数来决定的

#  5.使用 multiprocessing 库来试一下，在单独的进程中执行异步计算操作

if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()
    apply_async = pool.apply_async

    # Run the test function
    test()

#  6.将复杂的控制流隐藏到生成器函数背后
#   如，在 contextlib 中的 @contextmanager 装饰器使用了一个令人费解的技巧，通过 一个 yield 语句将进入和离开上下文管理器粘合在一起
#   另外非常流行的 Twisted 包 中也包含了非常类似的内联回调






































