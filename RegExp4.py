import re


def login_valid(login):

    pattern = r"[a-zA-Z0-9]{2,11}$"
    match = re.match(pattern, login)
    if match:
        return True
    else:
        return False



print(login_valid('Jack12345'))
print(login_valid('Jack123456789'))