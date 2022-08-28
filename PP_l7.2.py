def gen_range(start, stop):
    i = start
    while i < stop:
        yield i
        i += 1


x = gen_range(1, 100)

for item in x:
    print(item)
