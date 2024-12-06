# slice
for i in range(5, 0, -1):
    print(i)

# start stop step
s1 = '12434544678944'
s2 = s1[0:6:2]  # step is 2
print(s2)

print(max(1, 9, 75))
print(s1.index('7'))  # 返回第一次出现的索引位置
print(s1.count('4'))  # 返回包含的次数

# list 的元素类型可以不相同
lst = [1 ,2, 'asd', 4.33]
print(lst)
lst2 = list('123')
print(lst2)
print(list(range(1, 5, 2)))
print(lst + lst2)
# del lst

# 列表的遍历
for item in lst:
    print(item)
for i in range(0, len(lst)):
    print(lst[i], end = ' ')
print()
for index, item in enumerate(lst):
    print(index, item)
lst.append(1234)
print(lst)
lst.insert(0, 'hello')
print(lst)
print(lst.pop(0))
print(lst, id(lst))
lst.reverse()
print(lst)
# 列表的排序
lst = [123, 356, 657, 123, 826, 82789, 1456]
lst.sort(reverse = True)
print(lst)
new_lst = sorted(lst)  # 这个内置函数会返回一个新的列表
print(new_lst)
# 列表生成式
import random
lst = [item for item in range(1, 10)]
print(lst)
lst = [random.randint(1, 100) for _ in range(1, 10)]
print(lst)
lst = [item for item in range(1, 10) if item % 2 == 0]
print(lst)
# 二维列表

# tuple 速度比列表快，可以作为字典的键
tp1 = tuple([1, 2, 3])
print(tp1)
tp2 = 123,
print(type(tp2))  # 这样居然也能声明一个元组类型，逗号不能省略
# 元组生成式
tp1 = (i for i in range(1, 10))  # 这里返回的是一个生成器对象，并不是元组
tp2 = tuple(tp1)
print(tp2)

# 字典 按照键值对的形式进行访问
d1 = {1: '12', 2: '45'}
print(d1)
lst1 = [1, 34, 44, 654]
lst2 = ['12', '123', '546', '5467']
zipobj = zip(lst1, lst2)
d2 = dict(zipobj)
print(d2)
d3 = dict(a=23, b=123)
print(d3)
# 元组也可以作为字典的键
t1 = (1, 2, 3)
print({t1: 666})

print(d2[34])  # 找不到会报错
print(d2.get(3444, '不存在'))  # 找不到会返回默认值 或 None
for i in d2.items():
    print(i, end = ' ')
print()

# set
s = {1, 2, 3}
print(s)
s = set(); # 创建一个空集合
print(s)
s = set('123456')  # 集合是无序的，跟字典是一样的
print(s)

A = {1, 2, 3, 8, 9}
B = {2, 3, 4, 5, 6}
print(A & B)
print(A | B)
print(A - B)
# 差集，不相交的部分
print(A ^ B)

A.add(666)
print(A)
A.remove(666)

