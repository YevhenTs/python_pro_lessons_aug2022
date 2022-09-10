import time


def decorator(n, adress):
    def wrapped(f):
        def my_function(*args):
            count = 1
            start = time.time()
            while count <= n:
                f(*args)
                count += 1
            end = time.time()
            with open(adress, 'w') as g:
                print(f'{n} times per {end - start} s.', file=g)
        return my_function
    return wrapped


@decorator(10_000_000, 'timing.txt')
def mul(a, b):
    return a * b


mul(361233, 70914353)
mul(36123, 709213)
mul(36345, 709213)
mul(36123, 70921)
mul(362342, 70932423)
