from functools import reduce

def a_line(a,b):
    return lambda x:a *x+b

lf1=a_line(3,5)
print(lf1(10))
