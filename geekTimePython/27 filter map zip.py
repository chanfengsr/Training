from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7]

# filter
# Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
f = filter(lambda x: x > 2, a)
print("filter : %s" % list(f).__repr__())  # [3, 4, 5, 6, 7]
print()

# map 根据提供的函数对指定序列做映射
# Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
m = map(lambda x: x + 1, a)
print("map1 : %s" % list(m).__repr__())  # [2, 3, 4, 5, 6, 7, 8]

b = [1, 2, 3]
c = [4, 5, 6]
m2 = map(lambda x, y: x + y, b, c)
print("map2 : %s" % list(m2).__repr__())  # [5, 7, 9]
print()

# reduce 对参数序列中元素进行累积
# Apply a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value.
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
# ((((1+2)+3)+4)+5). If initial is present, it is placed before the items
# of the sequence in the calculation, and serves as a default when the sequence is empty.
r = reduce(lambda x, y: x + y, [2, 3, 4], 1)
print("reduce : %s" % r)
print()

# zip 将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
d = [1, 2, 3]
e = [4, 5, 6]
f = [4, 5, 6, 7, 8]
z1 = zip(d, e)
print("z1 : %s" % list(z1).__repr__())  # [(1, 4), (2, 5), (3, 6)]
z2 = zip(d, f)  # 元素个数与最短的列表一致
print("z2 : %s" % list(z2).__repr__())  # [(1, 4), (2, 5), (3, 6)]
z3 = zip(*zip(d, e))  # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
print("z3 : %s" % list(z3).__repr__())  # [(1, 2, 3), (4, 5, 6)]
print()

# 列表元素依次相连
g = ['a', 'b', 'c', 'd', 'e', 'f']
z4 = zip(g[:-1], g[1:])
# [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f')]
print("列表元素依次相连 : \n%s" % list(z4).__repr__())
