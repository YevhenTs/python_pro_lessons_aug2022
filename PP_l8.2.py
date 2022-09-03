import time


def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi(n-1)+fibonachi(n-2)


start1 = time.time()
print(fibonachi(30))
stop1 = time.time()
print('Recursive Fibonachi Time:', stop1-start1)


def mem_fibonachi_1():
    mem = {0: 0, 1: 1}

    def mem_fibonachi_2(n):
        if n not in mem:
            mem[n] = mem_fibonachi_2(n-1) + mem_fibonachi_2(n-2)
        return mem[n]

    return mem_fibonachi_2


start2 = time.time()
print(mem_fibonachi_1()(30))
stop2 = time.time()
print('Memoization Fibonachi Time:', stop2-start2)



