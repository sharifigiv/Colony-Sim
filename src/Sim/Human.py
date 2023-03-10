from random import choice

class Human:
    def __init__(self, x, y, strenght, isDiseased, colony):
        self.x = x
        self.y = y

        self.age = 0
        self.strenght = strenght
        self.productionrate = 0

        self.isAlive = True
        self.isDiseased = isDiseased

        self.colony = colony

    def fight(self, Person):
        if Person != None and Person.isAlive:
            if Person.colony.name != self.colony.name:
                if Person.strenght >= self.strenght:
                    self.kill()

                    self.colony.area.remove([self.x, self.y])
                    Person.colony.area.append([self.x, self.y])

                    return False

                else:
                    Person.kill()

                    Person.colony.area.remove([Person.x, Person.y])
                    self.colony.are.append([Person.x, Person.y])

                    return True

    def kill(self):
        self.isAlive = False
        self.colony.people.remove(self)
        self.colony.world.all_people.remove(self)

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

        child = Human(self.x, self.y + 5, self.strenght, child_disease, self.colony)

        return child

    def update(self):
        self.age += 0.01
        self.productionrate += 0.01

        if self.age > self.strenght:
            self.kill()

        if self.isDiseased:
            self.age *= 1.5

        if self.productionrate > 30:
            child = self.bread()
            self.colony.add_people(child)
