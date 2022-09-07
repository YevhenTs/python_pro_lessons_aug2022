s = 0


def decorator(f):
    def res(*args):
        global s
        f(*args)
        s += 1
        return s
    return res


@decorator
def mul(a, b):
    return a * b


print(mul(2, 3))
print(mul(2, 3))
print(mul(2, 3))
print(mul(2, 3))
l = mul(2, 3)
print(l)


print(f'Called {s} times')