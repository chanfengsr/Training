# 函数的闭包
# 计算 y = ax + b，其中 x 为频繁更改的变量
def a_line(a, b):
    return lambda x: a * x + b

lf1 = a_line(3, 5)
print(lf1(10))
