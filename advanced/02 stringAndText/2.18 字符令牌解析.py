# 字符令牌解析
## 将一个字符串，从左到右将其解析为一个令牌流

text = 'foo = 23 + 42 * 10'

## 为了令牌化字符串，不仅仅需要匹配模式，还得指定模式的类型，如将字符串像下面这样转化为序列对
tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'), ('NUM', '42'),
          ('TIMES', '*'), ('NUM', '10')]

## 1.利用命名捕获组的正则表达式来定义所有可能的令牌，包括空格
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
print('=========1=========')
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
print(master_pat)













