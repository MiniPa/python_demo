# 使用其他分隔符或行终止符打印

print('=========1=========')
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print(','.join(('ACME','50','91.5'))) # same with upper just for str
print('ACME', 50, 91.5, sep=',', end='!!\n')
print('ACME', 50, 91.5, end='') # 禁止换行
print()
print(type('str'))

print('=========2=========')
row = ('ACME', 50, 91.5)
# print(','.join(row))
print(','.join(str(x) for x in row))
print(*row, sep=',')

























