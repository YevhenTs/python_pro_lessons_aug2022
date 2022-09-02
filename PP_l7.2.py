def gen_range(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


x = gen_range(1, 100, 20)

for item in x:
    print(item)
