# 审查清理文本字符串

print('=========1=========')
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

## 1 清理空白字符
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None # Deleted
}
a = s.translate(remap)
print(a)










