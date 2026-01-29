# python 的 + - * / // ** % 运算符
from operator import truediv

c1 = 12
c2 = 13
print(c1, c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1 // c2)  # 向下取整

print(2 ** 10)  # 1024 指数运算
print(10 % 7)  # 3 指数运算

# string
s1 = 'abc'
s2 = "abc"
s3 = "I'm not Line."
s4 = 'I\'m not Line.'
print(s1, s2, s3, s4)

# slice
s5 = 'This is Test Slice'
print(s5[0:])

# if
if len(s5) > len(s1):
    print(s5[:-2])
elif len(s2) <= len(s5[0:2]):
    print(s5[:-2])
else:
    print(s5[:-3])


