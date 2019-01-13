# 将print() 输出重定向到一个文件

with open('5.02out.txt', 'wt') as f:
    print('hello world!', file=f)
    print('重定向成功，文件必须是text模式打开的')



