# 运行时弹出密码输入提示
import getpass

user = getpass.getuser()
passwd = getpass.getpass()

def svc_login(user, passwd):
    '''自定义登录'''

if svc_login(user, passwd):
    print("OK")
else:
    print("Sorry")

## getUser() 不会弹出用户名输入提示，会根据该用户的shell环境或者依据本地系统的密码库(支持pwd模块的平台) 使用当前用户登录名

## 弹出用户名提示
user = input('Enter your username: ')











