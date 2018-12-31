## 获取用户的输入，命令行输出管道、重定向文件、命令行中传递一个文件名或文件名列表给脚本

import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
## 可以用前面提到的所有方式为上面脚本提供输入, 可以像下面这样调用它

# $ ls | ./filein.py # Prints a directory listing to stdout.
# $ ./filein.py /etc/passwd # Reads /etc/passwd to stdout.
# $ ./filein.py < /etc/passwd # Reads /etc/passwd to stdout.


## fileinput.input() 创建并返回一个 FileInput 类的实例， 可以被当作上下文管理器使用
## 将FileInput作为上下文管理器使用，可确保它不再使用文件时候，能自动关闭

import fileinput
with fileinput.input('/etc/passwd') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')

# /etc/passwd 1 #
# /etc/passwd 2 # User Database #
# /etc/passwd 3 #









