from random import choice

class Colony:
    def __init__(self, name, color, world):
        self.name = name
        self.color = color

        self.people = []
        self.worl = world

    def add_people(self, Person):
        self.people.append(Person)
        self.world.new_people(Person)

        Person.colony = self.name

    def update():
        for person in self.people:
            direction = choice([1, 2, 3, 4])
            person.update()

            if direction == 1:
                if self.world.check_place(self.x - 5, self.y):
                    person.x -= 5
                    
                else:
                    person.fight(self.world.get_person(self.x - 5, self.y))

            if direction == 2:
                if self.world.check_place(self.x + 5, self.y):
                    person.x += 5

                else:
                    person.fight(self.world.get_person(self.x, self.y + 5))

            if direction == 3:
                if self.world.check_place(self.x, self.y - 5):
                    person.y -= 5

                else:
                    person.fight(self.world.get_person(self.x, self.y - 5))

            if direction == 4:
                if self.world.check_place(self.x, self.y + 5):
                    person.y += 5

                else:
                    person.fight(self.world.get_person(self.x, self.y + 5))
