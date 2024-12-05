# if elif else
print('123' if True else '456')
print('123' if False else '456')
score = 8
if score >= 90:
    print('good')
elif score >= 60:
    print('well')
else:
    print('no no no')

# mathch 3.11 版本引入的新特性
score = 'B'
match score:
    case 'A':
        print('GOOD')
    case 'B':
        print('well')

# for循环
for i in  'hello':
    print(i, end = '')
for i in range(0, 10):
    print(i, end = '')
print()
# 水仙花数 100-999
for i in range(100, 1000):
    s = str(i)
    x = int(s[0])
    y = int(s[1])
    z = int(s[2])
    if x**3 + y**3 + z**3 == i:
        print('水仙花：', i)
print(sum(range(0, 101, 2)))  # 2 代表步长，每隔一个数求和

# while 循环
i = 0
while i < 5:
    print(i, end = '')
    i += 1

# pass 使语法结构完整不报错，相当于todo()!
for i in range(1, 5):
    pass
