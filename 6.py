# class private_member
class MyClass:
    def __init__(self):
        self.__private_var = 42

obj = MyClass()
# 以下访问将会抛出 AttributeError
# print(obj.__private_var)
# 但可以通过 name mangling 访问
print(obj._MyClass__private_var)  # 输出 42