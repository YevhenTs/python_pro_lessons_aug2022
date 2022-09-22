import re


text = (str(input('Input text: ')))
pattern = r"[Rr][bB]{1,}[Rr]"
match = re.findall(pattern, text)

if match:
    print(match)
else:
    print('pattern not found')