#
person = {"name":"Lucy","age":23}

#字符串拼接
sentence = "My name is" + person["name"]+",and my age is "+str(person["age"])
print(sentence)

#format替换 元素位置可忽略不写
sentence_format_no_cursor = "My name is {0} and I am  {1} year old.".format(person["name"],person["age"])
sentence_format = "My name is {0} and I am  {1} year old.".format(person["name"],person["age"])
print(sentence_format_no_cursor)
print(sentence_format)

#format 写法3
sentence3 = "My name is {0[name]} and my age is {1[age]}".format(person,person)
sentence4 = "My name is {0[name]} and my age is {0[age]}".format(person)
print(sentence3)
print(sentence4)

line = "h1"
content = "This is a line."
code_html = "<{0}>{1}</{0}>".format(line, content)
print(code_html)


#类定义中使用
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Tom", 28)
_person_sentence = "My name is {0.name} and I am  {0.age} year old.".format(p1)
print(_person_sentence)

#直接声明的形式
sentence5 = "My name is {name} and I am  {age} year old.".format(name="p1.name", age="p1.age")
print(sentence5)

#拆包
person1 = {"name":"Jenn","age":25}
sentence6 = "My name is {name} and I am {age} year old.".format(**person1)
print(sentence6)

#数字不全为2位
for i in range(1,11):
    sentence = "This value is {:02}".format(i)
    print(sentence)

#小数位截取格式化
PI = 3.14159265
sentence7 = "PI is equals to {:.2f}".format(PI)
print(sentence7)

#整数按,分割并且保留两位小数
sentence8 = "1M equals to {:,.2f} kb".format(1024)
print(sentence8)

import datetime
my_date = datetime.datetime(2026, 11, 16, 23, 59, 59)
print(my_date)

datetime1 = "{:%B %d, %Y}".format(my_date)
print(datetime1)

sentence9 = "The datatime of {0:%B %d, %Y} Weekday is {0:%A} and is the {0:%j} days of year".format(my_date)
print(sentence9)