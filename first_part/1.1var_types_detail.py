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
print(10 % 7)  # 3 取模运算


# string
s1 = 'abc'
s2 = "abc"
s3 = "I'm not Line."
s4 = 'I\'m not Line.'
print(s1, s2, s3, s4)

#不转义成特殊字符 在字符串前使用 r
print(r'D:\install\cache')

#相邻两个字符串字面量会自动合并(不能用于赋值后变量或表达式，表达式或变量需要用 +)
onionStr = 'py' 'thon'
print(onionStr)
print(onionStr + ' tourist')

# slice(切片会自然处理越界)
s5 = 'This is Test Slice'
print(s5[0:])

#字符串immutable,不能修改为某个位置索引设置值
# onionStr[2] = 'j' #TypeError: 'str' object does not support item assignment
newOnionStr = 'P'+onionStr[1:]
print(newOnionStr)
len(newOnionStr)


# if
if len(s5) > len(s1):
    print(s5[:-2])
elif len(s2) <= len(s5[0:2]):
    print(s5[:-2])
else:
    print(s5[:-3])


