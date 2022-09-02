def numbers_sum(sequence, predicate):
    sequence = predicate(sequence)
    sum = 0
    for element in sequence:
        sum += element
    return sum


def predicate_one(number):
    return number * 3


seq = [0, 7, 4, 11, 24, 3]
a = numbers_sum(seq, predicate_one)
print(a)
