import re


def email_valid(mail):

    pattern = r'^[a-zA-Z0-9](-?[a-zA-Z0-9_])+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$'
    match = re.match(pattern, mail)
    if match:
        return True
    else:
        return False



print(email_valid('this_ismyemail@gmail.com'))
print(email_valid('-this_isnotmyemail@gmail.com'))
