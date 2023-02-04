from random import choice

class Colony:
    def __init__(self, name, color, world):
        self.name = name
        self.color = color

        self.people = []
        self.world = world

    def add_people(self, Person):
        self.people.append(Person)
        self.world.new_people(Person)

        Person.colony = self

    def update(self):
        for person in self.people:
            direction = choice([1, 2, 3, 4])
            person.update()

            if direction == 1:
                if self.world.check_place(person.x - 5, person.y):
                    person.x -= 5
                    
                else:
                    if self.world.exists(person.x - 5, person.y):
                        if not self.world.check_place(person.x - 5, person.y):
                            person.fight(self.world.get_person(person.x - 5, person.y))

            if direction == 2:
                if self.world.check_place(person.x + 5, person.y):
                    person.x += 5

                else:
                    if self.world.exists(person.x + 5, person.y):
                        if not self.world.check_place(person.x + 5, person.y):
                            person.fight(self.world.get_person(person.x + 5, person.y))

            if direction == 3:
                if self.world.check_place(person.x, person.y - 5):
                    person.y -= 5

                else:
                    if self.world.exists(person.x, person.y - 5):
                        if not self.world.check_place(person.x, person.y - 5):
                            person.fight(self.world.get_person(person.x, person.y - 5))

            if direction == 4:
                if self.world.check_place(person.x, person.y + 5):
                    person.y += 5

                else:
                    if self.world.exists(person.x, person.y + 5):
                        if not self.world.check_place(person.x, person.y + 5):
                            person.fight(self.world.get_person(person.x, person.y + 5))
