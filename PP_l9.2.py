my_function = []


def add_function(f):
    my_function.append(f)
    return f


@add_function
def geo(first, n):
    numbers = []
    second_number = 2
    index = 1
    while index <= n:
        next_number = first * second_number
        first = next_number
        index = index + 1
        numbers.append(next_number)
    return numbers


print(my_function)

for f in my_function:
    print(f(1, 10))