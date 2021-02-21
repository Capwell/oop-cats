class Cat:
    mew: str = 'муурр'*4

    def make_happy(self) -> str:
        return self.mew


class LuckyCat(Cat):
    lucky_mew: str = 'Я сыт, мне тепло, я сплю'

    def make_happy(self) -> str:
        return self.lucky_mew


kuzya = LuckyCat()
print(kuzya.make_happy())
