# 给函数库增加日志功能，但又不能影响到哪些不使用日志功能的程序

## 对于想要执行日志操作的函数库，应创建一个专属logger对象，并初始化配置

# somelib.py
import logging
log = logging.getLogger(__name__)
# 绑定空处理器到刚创建的logger对象上，空会忽略调用所有的日志消息
log.addHandler(logging.NullHandler)

def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')

## import somelib
## somelib.func()
# 如果配置过日志系统，日志消息打印就开始生效

## 函数库的日志配置可以是互相独立的

import logging
logging.basicConfig(level=logging.ERROR)

# Change the logging level for 'somelib' only
logging.getLogger('somelib').level=logging.DEBUG
# somelib.func() ## 此处配置只在当前模块生效

## 参考 https://docs.python.org/3/howto/logging.html





















