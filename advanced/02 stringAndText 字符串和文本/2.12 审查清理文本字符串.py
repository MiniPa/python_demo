# 审查清理文本字符串

print('=========1=========')
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

## 1 清理空白字符
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
a = s.translate(remap)
print('=========2=========')
print(a)

## 2 清除所有和音符
import unicodedata
import sys

print('=========3=========')
# dict.fromkeys() 构造一个字典，每个 Unicode 和音 符作为键，对应的值全部为 None
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print(cmb_chrs)
# unicodedata.normalize() 将原始输入标准化为分解形式字符
b = unicodedata.normalize('NFD', a)
print(b)
# 调用 translate 函数删除所有重音符
b = b.translate(cmb_chrs)
print(b)

## 3 构造将所有Unicode数字字符映射到对应ASCII字符上的表格
print('=========4=========')
digitmap = {
    c: ord('0') + unicodedata.digit(chr(c))
    for c in range(sys.maxunicode)
    if unicodedata.category(chr(c)) == 'Nd'
}
print(len(digitmap))
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

## 4 I/O解码、编码函数
print('=========5=========')
print(a)
# 下面的标准化操作将原来的文本分解为单独的和音符
b = unicodedata.normalize('NFD', a)
c = b.encode('ascii', 'ignore').decode('ascii')
print(c)


## 文本字符清理最该考虑的是性能问题，
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s
#如上方法的执行会比 translate()或者正则表达式快很多


