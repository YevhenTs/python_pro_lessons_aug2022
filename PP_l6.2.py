class Goods:
    """
    Defines class Goods
    """

    def __init__(self, price, description, dimensions):

        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.description}:{self.price} USD, dimensions:{self.dimensions}'


class Buyer:

    def __init__(self, surname, name, number):

        self.name = name
        self.surname = surname
        self.number = number

    def __str__(self):
        return f'{self.name} {self.surname}, number = {self.number}'


class CartIterator:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]

        else:
            raise StopIteration

    def __iter__(self):
        return self


class Cart:

    def __init__(self, cart):
        self.title = cart
        self.goods = []
        self.buyers = []

    def add_buyer(self, buyer: Buyer):
        self.buyers.append(buyer)

    def add_goods(self, product: Goods):
        self.goods.append(product)

    def summa(self):
        s = 0
        for item in self.goods:
            s += int(item.price)
        return s

    def __str__(self):
        res = f'{self.title}\n'
        res += '\n'.join(map(str, self.buyers))
        res += '\n'
        res += '\n'.join(map(str, self.goods))
        res += f'\nTotal: {self.summa()} USD.'
        return res

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > len(self.goods):
                raise IndexError()
            else:
                return self.goods[index]

        if isinstance(index, slice):
            start = 0 if index.start == None else index.start
            stop = len(self.goods) if index.stop == None else index.stop
            step = 1 if index.step == None else index.step
            temp_list = []
            if start < 0 or stop > len(self.goods):
                raise IndexError()
            else:
                for i in range(start, stop, step):
                    temp_list.append(self.goods[i])
                return temp_list
        raise TypeError

    def __len__(self):
        return len(self.goods)

    def __iter__(self):
        return CartIterator(sh_cart.goods)


product_1 = Goods('1000', 'Iphone 12', '146.7 x 71.5 x 7.4 mm')
product_2 = Goods('900', 'Iphone 11', '150.9 x 75.7 x 8.3 mm')
b_1 = Buyer('Ivanov', 'Ivan', '380951234567')

sh_cart = Cart('Shopping cart')
sh_cart.add_buyer(b_1)
sh_cart.add_goods(product_1)
sh_cart.add_goods(product_2)
print(sh_cart)

print('\n check 1 \n')
a = sh_cart[1:2]
for i in a:
    print(i)

print('\n check 2 \n')
for i in sh_cart:
    print(i)