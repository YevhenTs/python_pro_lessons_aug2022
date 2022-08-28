def geo_prog_gen(n):
    first_number = 1
    second_number = 2
    index = 1
    while index <= n:
        next_number = first_number * second_number
        first_number = next_number
        index = index + 1
        yield next_number
    return


for i in geo_prog_gen(10):
    print(i)