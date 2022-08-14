class NegNumExcept(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'


try:
    price = int(input('Input price: '))
    if price < 0:
        raise NegNumExcept('Negative number value!')

except NegNumExcept as err:
    print(err)
except ValueError:
    print('Price is not number!')