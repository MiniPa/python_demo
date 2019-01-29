# 5.05 文件不存在才能写入

with open('5.05somefile.txt', 'wt') as f:
    f.write('Hello\n')

try:
    with open('5.05somefileout.txt', 'xt') as f:
        ''' xb、xt 来解决问题 '''
        f.write('Hello\n')
except FileExistsError as e:
    print('except:', e)

## 测试文件是否存在
import os
if not os.path.exists('5.05somefileout.txt'):
    with open('5.05somefileout.txt', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')




























