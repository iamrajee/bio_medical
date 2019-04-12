from multiprocessing import Process

def f(name):
    while True:
        # pass
        print("2", end="")
def f2(name):
    while True:
        # pass
        print("6", end="")

if __name__ == '__main__':
    print("0", end="")
    p = Process(target=f, args=('bob',))
    p2 = Process(target=f2, args=('bob',))
    print("1", end="")
    p.start()
    print("5", end="")
    p2.start()
    print("3", end="")
    p.join()
    p2.join()
    print("4", end="")