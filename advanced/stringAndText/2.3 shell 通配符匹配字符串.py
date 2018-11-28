# 使用 Unix Shell 中常用的通配符 (比如 *.py , Dat[0-9]*.csv 等) 去匹配文 本字符串
from fnmatch import fnmatch, fnmatchcase

print('=========1===========')
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('foo.txt','?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
names2 = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(names2)

## fnmatch()使用底层操作系统的大小写敏感规则（不同系统不相同）进行匹配模式
print(fnmatch('foo.txt', '*.TXT'))  # Mac:False Windows:True
print(fnmatchcase('foo.txt', '*.TXT')) # 完全按照大小写匹配

## 处理非文件名字符串
print('=========2===========')
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
addresses2 = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(addresses2)
addresses3 = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(addresses3)













