def decorator(f):
    s = 0

    def res(*args):
        nonlocal s
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