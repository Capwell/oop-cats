class Cat:
    mew: str = 'муурр'*4

    def make_happy(self) -> str:
        return self.mew


print(Cat.mew)

kuzya = Cat()
# print(kuzya.mew)
#
# Переопределим свойства объекта (экземпляра класса)
kuzya.mew = 'мяу'
print(kuzya.mew)

# Свойство класса осталось прежним
print(kuzya.make_happy())

# Сделаем счастливым безымянного кота
print(Cat().make_happy())
