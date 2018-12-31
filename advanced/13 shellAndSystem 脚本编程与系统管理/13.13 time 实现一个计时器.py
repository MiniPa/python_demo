# 实现一个计时器

import time


class Timer:
    '''一个有启动、停止、重置功能的计时器，在elapsed中记录消耗时间'''

    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already Started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

def countdown(n):
    while n > 0:
        n -= 1

# Use 1: Explicit start/stop

t = Timer()
t.start()
countdown(1000000)
t.stop()
print(t.elapsed)

# Use 2: As a context manager
with t:
    countdown(1000000)
print(t.elapsed)

with Timer() as t2:
    countdown(1000000)
print(t2.elapsed)

## 底层时间函数的考虑
# time.time() 或 time.clock() 计算时间的精度因操作系统的不同而不同
# 使用time.perf_counter()确保使用系统上最精确的计时器

## 上述代码 Timer记录的时间是钟表时间，包含了所有的休眠时间
# 只计算CPU运行该进程的时间，应用time.process_time()来代替

t = Timer(time.process_time)
with t:
    countdown(1000000)
print(t.elapsed)

## time.perf_counter() 和 time.process_time() 都会返回小数形式的秒数时间。
# 计算两者的差值能到时间增量


















