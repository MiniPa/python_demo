# 数字格式化输出，并控制数字的位数、对齐、千分分隔符等其他细节

print('=========1===========')
x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, '0,.1f'))

print('=========2===========')
# 使用指数计法
print(format(x, 'e'))
print(format(x, '0.2E'))

## 同时指定宽、精度 '[<>^]?width[,]?(.digits)?'  ?代表可选部分
# 同样的格式也被用在字符串的 format()
print('The value is {:0,.2f}'.format(x))

## 上面内容同样适用于 float 和 Deciamal
# 指定数字位数后，结果会根据 round()函数同样规则 四舍五入后返回
print('=========3===========')
print(format(x, '0.1f'))
print(format(-x, '0.1f'))

## 包含千分位的格式化和本地化没有关系，需要根据地区显示千位符，可以自己调查下locale模块中的函数
swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators)) # '1.234,56789'

## % 来格式化数字
print('=========4===========')
print('%0.2f' % x)
print('%10.1f' % x )
print('%-10.1f' % x )

## format 比 % 多一些特性，比如提供千分位支持等














