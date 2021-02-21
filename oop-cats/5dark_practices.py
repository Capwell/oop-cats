class Cat:
    mew: str = 'муурр'*4

    def make_happy(self) -> str:
        return self.mew


kuzya = Cat()
# Легально
kuzya.mew = 'мур-мяу'*5
print(kuzya.mew)


# Темные практики
kuzya.paw = 5
print(kuzya.paw)
