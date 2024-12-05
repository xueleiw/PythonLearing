# 字符串的索引从左往右和从右往左从 1 和 -1 开始
s1 = "hello"
print(s1[1], s1[-4])
print(s1[0:3])  # 左开右闭区间
print(s1[:3])
s2 = s1 * 3   # 代表复制多少次
print(s2)
print('hel' in s1) # 用in检查一个字符串是否在另一个字符串里面，返回true or false

# True False 首字母大写
print(int(True))  # 相当于 1
print(int(False))
print(bool(10), bool(0.1), bool(0), bool(None), bool(''))  # 非0值均为True
print(ord('a'))  # 字符 转成Unicode码


# eval 去掉字符串两边的引号，经常和input函数一起使用，获取用户输入的数值
a = "1+4"
b = eval(a)
print('计算结果：', b)

# // **
print('除法 ' + f"{10 / 3:.3f}")
print('整除: ', 10 // 3)
print('幂运算', 2**4)

# 链式赋值
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)

# and or not
print('逻辑运算：', '-' * 44)
print(3 > 2 and 4 > 3)
print(not False)
print(~False)  # 按位取反

#
print('位运算：', '-' * 44)
print(2 << 10)
print(-1023 >> 12)  # 补码形式的算术右移，最后都会是 -1


