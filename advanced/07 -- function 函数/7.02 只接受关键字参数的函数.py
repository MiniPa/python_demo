# 只接受关键字参数的函数

# 将强制关键字参数放到某个 * 参数或者单个 * 后面就能达到这种效果
def recv(maxsize, *, block):
    'Receives a message'
    pass

recv(1024, True) # TypeError
recv(1024, block=True) # Ok

# 在接受任意多个位置参数的函数中指定关键字参数
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
        return m

minimum(1, 5, 2, -5, 10) # Returns -5
minimum(1, 5, 2, -5, 10, clip=0) # Returns 0

# 使用强制关键字参数会比使用位置参数表意更加清晰，程序也更加具 有可读性
msg = recv(1024, False)
msg = recv(1024, block=False)
help(recv)
# Help on function recv in module __main__:
#     recv(maxsize, *, block)
#     Receives a message
































