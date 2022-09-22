import re


def valid(number):

    pattern = r"^\d{4}-\d{4}-\d{4}-\d{4}$"
    match = re.match(pattern, number)

    if match:
        return True
    else:
        return False


number = str(input("Input card number: "))
print(valid(number))