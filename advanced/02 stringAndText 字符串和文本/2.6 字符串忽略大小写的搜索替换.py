# 字符串忽略大小写替换
import re
text = 'UPPER PYTHON, lower python, Mixed Python'

print('=========1=========')
text2 = re.findall('python', text, flags=re.IGNORECASE)
print(text2)
text3 = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(text3)
## text3 可见替换字符串并不会自动跟被匹配的字符串大小写保持一致，使用下面的辅助函数

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
print('=========2=========')
text4 = re.sub('python', matchcase('snake'), text, flags = re.IGNORECASE)
print(text4)
## matchcase('snake') 返回了一个回调函数，参数必须是match对象
## sub() 除去接受一个替换字符串，也能接受一个回调函数







