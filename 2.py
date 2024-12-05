import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

# 中文也可以做变量名，但不推荐
阿斯 = 123
print(阿斯)

#
a = b = "1234"
print(id(a))  # 打印内存地址
print(id(b))  # 与a的地址相同

# constant
PI = 3.14  # 虽然是常量，但是也可以修改，一般不推荐

# 0b 0o 0x
a = 127
print(bin(a))
print(oct(a))
print(hex(a))
##
print(f"{a:b}")
print(f"{a:o}")
print(f"{a:x}")
print(f"{a:X}")

b = 1.0
print(type(b)) # 查看类型 type()

c = 1.12
d = 4.15
print(round(c + d, 6))
print(f"{c + d:.6f}")
print(int(c + d))

# 虚数的表示
a = 123 + 456j
print(a.real, a.imag)

# 字符串
info = '''
name: wxl
    id: 001
'''
info = """
name: wxl
id: 002
"""
print(info)

# 转义字符  r 使转义字符失效
print('asdf\n1234')
print('asdf\t1234')
print('a\nb\nc\n')
print(r'a\nb\nc\n')

