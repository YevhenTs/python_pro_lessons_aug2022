def number_seq(first, n, predicat):
    numbers = predicat(first, n)
    for num in numbers:
        yield num


def geo(first, n):
    numbers = []
    second_number = 2
    index = 1
    while index <= n:
        yield first
        next_number = first * second_number
        first = next_number
        index += 1
        numbers.append(next_number)


print(number_seq(1, 11, geo))
print(geo(1, 10))

for num in number_seq(1, 11, geo):
    print(num)