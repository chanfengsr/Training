import threading
import time
from threading import current_thread


def myThread(*arg1):
    print("%s - %s --> %s" % (current_thread().getName(), 'start', arg1[1]))
    time.sleep(1)
    print("%s - %s" % (current_thread().getName(), 'stop'))


for i in range(1, 6, 1):
    t1 = threading.Thread(target=myThread, args=(i,i))
    t1.start()
    # t1.join()

print("%s - %s" % (current_thread().getName(), 'end'))
