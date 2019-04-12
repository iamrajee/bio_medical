import threading
# import time
# from time import *
from time import sleep
def f():
    while True:
        print("2", end="")
        # sleep(1)
    # print("2", end="")
def f2(name):
    while True:
        print("6", end="")
        # sleep(1)
    # print("6", end="")

if __name__ == '__main__':
    print("0", end="")
    p = threading.Thread(target=f, args=())
    p2 = threading.Thread(target=f2, args=('bob',))
    print("1", end="")
    p.start()
    print("5", end="")
    p2.start()
    print("3", end="")
    p.join()
    p2.join()
    print("4", end="")