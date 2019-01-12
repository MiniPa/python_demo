# 顺序迭代合并后的排序迭代对象

## 有一系列排序序列，将之合并后得到一个排序序列并在上面迭代遍历

import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

print('=========1==========')
for c in heapq.merge(a, b):
    '''将一系列排序序列合并为一个最终的排序序列，并遍历'''
    print(c)

## heapq.merge 可迭代特性意味着它不会立马读取所有的序列，意味着你可以在非常长的序列中使用它
with open('sorted_file_1', 'rt') as file1, \
        open('sorted_file_2', 'rt') as file2, \
        open('merged_file', 'wt') as outf:
            for line in heapq.merge(file1, file2):
                outf.write(line)

## heapq.merge() 需要所有输入序列必须是经过排序的
#  并不会预先读取所有的数据到堆栈中，或者预先排序，也不会对输入做任何排序检测
#  仅仅是检查所有序列的开始，并返回最小的那个
