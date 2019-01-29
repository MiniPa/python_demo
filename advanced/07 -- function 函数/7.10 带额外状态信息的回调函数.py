# 带额外状态信息的回调函数

## 代码中需要依赖到回调函数的使用 (比如事件处理器、等待后台任务完成后的 回调等)，并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到。

print('=========1=========')
## 如下是一个需调用回调函数的函数

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)

## 使用方式
def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result) ## Got: 5
apply_async(add, ('hello', 'world'), callback=print_result) ## Got: helloworld

## print_result() 只接受一个参数 result, 当你想让回调函数访问其他变量或特定环境的时候，就会遇到麻烦。
#  让回调函数访问外部信息

print('=========2=========')
#  方法一、使用一个绑定方法来代替一个简单函数
#  下面的类会保存一个内部序列号，每接到一个result时候序列号加1

class ResultHandler:

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

## 使用方式，先创建一个实例，然后用它的 handler() 绑定方法来做为回调函数
r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler) # [1] Got: 5
apply_async(add, ('hello', 'world'), callback=r.handler) # [2] Got: helloworld

print('=========3=========')
#  方法二、作为类的替代，可以使用一个闭包捕获状态值
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

## 使用方式，
handler = make_handler()
apply_async(add, (2, 3), callback=handler) # [1] Got: 5
apply_async(add, ('hello', 'world'), callback=handler) # [2] Got: helloworld

print('=========4=========')
#  使用协程 【important】
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

## 使用方式 对于协程，使用 send() 作为回调函数
handler = make_handler()
next(handler) # Advance to the yield
apply_async(add, (2, 3), callback=handler.send) # [1] Got: 5
apply_async(add, ('hello', 'world'), callback=handler.send) # [2] Got: helloworld

print('=========5=========')
## 基于回调函数的软件通常都会变得非常的复杂，原因：1.回调函数通常会和请求执行的代码断开，因此请求执行和处理结果之间的执行环境实际上已经丢失了。
#  如果你想让回调函数连续执行多步操作，必须解决如何保存和恢复相关的状态信息了。

#  至少有两种主要方式来捕获和保存状态信息，你可以在一个对象实例 (通过一个绑 定方法) 或者在一个闭包中保存它。
#  两种方式相比，闭包或许是更加轻量级和自然一点，因为它们可以很简单的通过函数来构造。它们还能自动捕获所有被使用到的变量。因 此，你无需去担心如何去存储额外的状态信息 (代码中自动判定)。
#  用一个协程来作为一个回调函数就更有趣了，它跟闭包方法密切相关，显得更加简洁，因为总共就一个函数而已。

































































