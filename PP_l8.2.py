import timeit

var_1 = """
def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi(n-1)+fibonachi(n-2)
        
print(fibonachi(30))
"""


print(timeit.timeit(var_1, number=5))

var_2 = """
def mem_fibonachi_1():
    mem = {0: 0, 1: 1}

    def mem_fibonachi_2(n):
        if n not in mem:
            mem[n] = mem_fibonachi_2(n-1) + mem_fibonachi_2(n-2)
        return mem[n]

    return mem_fibonachi_2
    
print(mem_fibonachi_1()(30))
"""


print(timeit.timeit(var_2, number=5))



