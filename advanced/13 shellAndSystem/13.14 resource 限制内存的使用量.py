# 限制内存的使用量

import signal
from resources import resource
import os

def time_exceeded(signo, frame):
    print("Time's up!")
    raise SystemExit(1)

def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)

if __name__ == '__main__':
    set_max_runtime(15)
    while True:
        pass

## 程序运行时，SIGXCPU 信号在时间过期时被生成，然后执行清理并退出


## 限制内存使用，可设置内存总值即可
from resources import resource

def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))
# 程序运行到没有多余内存时会抛出 MemoryError 异常

## setrlimit() 被用来设置特定资源上的软限制和硬限制
# 软限制 超过时候，操作系统会发送一个信号来限制或通知该进程
# 硬限制 用来指定软限制能设定的最大值

## setrlimit() 还能被用来设置子进程数量、打开文件数、以及类似系统资源的限定

## note 本节内容只适合 Unix系统











