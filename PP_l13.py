import abc


class Prime(abc.ABC):

    @abc.abstractmethod
    def prime(self, n):
        pass

    @classmethod
    def register(cls, Prime3):
        pass


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

