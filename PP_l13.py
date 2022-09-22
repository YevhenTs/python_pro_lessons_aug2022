import abc


class Prime(abc.ABC):

    @abc.abstractmethod
    def prime(self, n):
        pass

    @classmethod
    def __subclasshook__(abc_class, Prime3):
        for sub_class in Prime3.__mro__:
            for property_name in sub_class.__dict__:
                if property_name == "prime":
                    return True
        return False


class Prime2(Prime):

    def prime(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


class Prime3:

    def prime(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True



print(Prime2().prime(38))
print(Prime3().prime(47))

