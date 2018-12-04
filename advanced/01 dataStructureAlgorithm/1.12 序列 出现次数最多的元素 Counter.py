# 寻找序列中出现次数最多的元素 collections.Counter
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

## Counter 可以接受任意由可hashable元素构成的序列对象，Counter底层是一个字典
print('==========1==========')
word_counts = Counter(words)
top_three = word_counts.most_common(3) # 查找频率最高的几位
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]
print(word_counts['look'])
print(word_counts['eyes'])

## 可手动增加计数
print('==========2==========')
word_counts['look'] += 10
print(word_counts['look'])

morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)

## Counter 可以和数学操作相结合
print('==========3==========')
a = Counter(words)
b = Counter(morewords)
c = a + b
print(c)
d = a - b
print(d)






