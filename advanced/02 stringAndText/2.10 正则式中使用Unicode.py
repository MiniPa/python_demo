# 使用正则表达式处理文本，但关注的是Unicode字符的处理
import re

print('=========1=========')
num = re.compile('\d+')
print(num.match('123')) # ASCII digits
print(num.match('\u0661\u0662\u0663')) # Arabic digits

## 想在模式中包含指定的Unicode字符，可以使用Unicode字符对应的转义序列(如：\uFFF 或 \UFFFFFFF)
## 下面是一个匹配几个不同阿拉伯编码页面中所有字符的正则表达式
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

## 执行匹配和搜索操作时候，最好先标准化并清理所有文本为标准化格式
## 也应该注意些特殊情况，如在忽略大小写匹配和大小写转换时的行为
print('=========2=========')
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s)) # matches
print(pat.match(s.upper())) # doesn't match
print(s.upper()) # case folds

## 建议使用三方库来处理Unicode相关问题，否则你会崩溃





