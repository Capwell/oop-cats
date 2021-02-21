class Cat:
    __mew: str = 'муурр'*4

    def make_happy(self) -> str:
        return self.__mew


kuzya = Cat()
print(kuzya.__mew)  # Не сработает
# print(kuzya.mew)
print(kuzya.make_happy())
