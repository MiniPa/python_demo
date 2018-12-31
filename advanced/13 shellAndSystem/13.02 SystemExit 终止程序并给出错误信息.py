# 终止程序并给出错误信息

# 想向标准错误打印一条消息，并返回一个非0状态码来终止程序运行

# 如下将会终止程序，抛出SYstemExit异常，错误消息'It failed'将会在sys.stderr中打印，程序以状态码1退出
raise SystemExit('It failed!')

# 想终止一个程序，可以如下
import sys
sys.stderr.write('It failed! \n')
raise SystemExit(1)















