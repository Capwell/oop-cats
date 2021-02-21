class Cat:
    def __init__(self, mew: str = 'муурр'*4) -> None:
        self.mew = mew

    def make_happy(self) -> str:
        return f'{self.mew}'


class NeedsCat(Cat):
    def __init__(self, needs: str) -> None:
        super().__init__()
        self.needs = needs

    def make_happy(self) -> str:
        return f'{self.mew}, {self.needs}'


murzik = NeedsCat('Дай пожрать!')
print(murzik.make_happy())
