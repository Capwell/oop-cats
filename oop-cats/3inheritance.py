class Cat:
    mew: str = 'муурр'*4

    def make_happy(self) -> str:
        return self.mew


class LuckyCat(Cat):
    pass


kuzya = LuckyCat()
print(kuzya.make_happy())
