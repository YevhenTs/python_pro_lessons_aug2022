def prime_numbers_gen(n):
    for i in range(2, n + 1):
        for j in range(2, i):
            if not i % j:
                break
        else:
            yield i


list1 = list(prime_numbers_gen(200))
print(list1)