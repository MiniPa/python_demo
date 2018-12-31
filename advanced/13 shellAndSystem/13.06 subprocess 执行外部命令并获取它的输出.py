# 执行外部命令 并获取它的输出

import subprocess

## 执行一个命令，并将结果用字符串的形式返回
out_bytes = subprocess.check_output(['netstat', '-a'])

## 用文本形式返回
out_text = out_bytes.decode('utf-8')

## 如果执行的命令以非0码返回，就会抛异常
try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output # Output generated before error
    code = e.returncode # Return code

## 默认 check_output() 仅仅返回输入到标准输出的值，加入stderr可同时收集标准输出和错误输出
out_bytes = subprocess.check_output(['cmd','arg1','arg2'], stderr=subprocess.STDOUT)

## timeout=5 超时机制
try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'], timeout=5)
except subprocess.TimeoutExpired as e:
    print("nothing")


# 一般命令行执行不需要使用底层shell环境（如 sh、bash）
# 一个字符串 列表会被传递给一个低级系统命令，比如 os.execve()
# 如下让python 执行一个复杂的Shell命令

out_bytes = subprocess.check_output('grep python | wc > out', shell= True)

## note: shell 中执行命令会存在一定的风险，特别当参数来自用户输入时候，可用shlex.quote()将参数正确的用双引号引起来






# 更复杂的交互 采用subprocess.Popen
import subprocess

# Some text to send
text = b'''
hello world
this is a test goodbye
'''

## Launch a command with pipes
p = subprocess.Popen(['wc'], stdout = subprocess.PIPE, stdin = subprocess.PIPE)

## Send the data and get the output
stdout, stderr = p.communicate(text)

## To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')

## subprocess 对于以来 TTY 的外部命令不适合用
## 如不可以用来自动化一个用户输入密码的任务（如一个ssh会话），需要使用第三方模块，如 except的pexpect或类似










