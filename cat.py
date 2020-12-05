# This is terrible and you should never do this.

class Cat:

    def __init__(self, name):
        self.name = name

    def meow(self):
        print("Meow")

    def eat(self, food):
        print(f"Eats {food}")

cat = Cat("Fluffy")
cat.meow()
cat.eat("salmon")
