from random import choice

class Human:
    def __init__(self, x, y, strenght, isDiseased, colony):
        self.x = x
        self.y = y

        self.strenght = strenght
        self.productionrate = 0

        self.isAlive = True
        self.isDiseased = isDiseased

        self.colony = colony

    def fight(self, Person):
        if Person.colony != self.colony:
            if Person.strenght >= self.strenght:
                self.kill()

            else:
                Person.kill()

    def kill(self):
        self.isAlive = False

    def make_sick(self):
        self.isDiseased = True

    def bread(self):
        self.productionrate = 0
        child_disease = False

        if self.isDiseased:
            child_disease = choice([1, 2])

            if child_disease == 1:
                child_disease = False 

            else:
                child_disease = True

        child = Person(self.x, self.y + 7, self.strenght, child_disease, self.colony)

        return child

    def update(self):
        self.age += 1
        self.productionrate += 1

        if self.age > self.strenght:
            self.kill()

        if self.isDiseased:
            self.age *= 1.5
