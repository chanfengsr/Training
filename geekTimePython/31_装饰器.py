import time
import datetime
from functools import wraps

def timmer(func):
    def wrapper():
        start_time = datetime.datetime.now()# time.time()
        func()
        stop_time = datetime.datetime.now()# time.time()
        print("运行时间是 %s" % (stop_time - start_time))
    return wrapper

@timmer
def i_can_sleep():
    time.sleep(1)

i_can_sleep()






def new_tips(argv):
    def tips(func):
        @wraps(func)
        def nei(a, b):
            print('start %s %s' % (argv, func.__name__))
            func(a, b)
            print('stop')
        return nei
    return tips


@new_tips('add_module')
def add(a, b):
    print(a + b)

@new_tips('sub_module')
def sub(a, b):
    print(a - b)

add(4, 5)
sub(7, 3)
print(add.__name__)



def t2(func):
    def n2(a,b):
        print('-->')
        func(a,b)
        print('<--')
    return n2


# @t2
def add2(a, b):
    print(a + b)

# add2(1,2)
t2(add2)(1,2)