# fractions 分数运算

from fractions import Fraction

print('=========1==========')
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)

## Getting numerator/denominator
c = a * b
print(c.numerator)
print(c.denominator)

## Converting to a float
print(float(c))

## Limiting the denominator of a value
print(c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)












