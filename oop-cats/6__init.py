class Cat:
    def __init__(self,
                 mew: str = 'муурр'*4,
                 paw: int = 4
                 ) -> None:
        self.mew = mew
        self.paw = paw

    def make_happy(self) -> str:
        return f'{self.mew} на {self.paw}х лапках'


kuzya = Cat()
print(kuzya.make_happy())
