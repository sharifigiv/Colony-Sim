from random import choice

class Colony:
    def __init__(self, name, color, area_color, world):
        self.name = name
        self.color = color
        self.area_color = area_color

        self.people = []
        self.world = world

        self.Started = True

        self.area = []

    def add_people(self, Person):
        self.people.append(Person)
        self.world.new_people(Person)

        Person.colony = self
        self.Started = False

        self.add_area([Person.x, Person.y])

    def add_area(self, Area):
        if Area not in self.area:
            self.area.append(Area)
            self.world.update_area(Area, self)

    def update(self):
        if len(self.people) == 0 and not self.Started:
            print(f"{self.name} destroyed!")
            self.world.colonies.remove(self)

        for person in self.people:
            if person.isAlive:
                direction = choice([1, 2, 3, 4])
                person.update()

                if direction == 1:
                    if self.world.check_place(person.x - 5, person.y):
                        person.x -= 5
                        self.add_area([person.x, person.y])
                        
                    else:
                        if self.world.exists(person.x - 5, person.y):
                            if not self.world.check_place(person.x - 5, person.y):
                                if person.fight(self.world.get_person(person.x - 5, person.y)):
                                    person.x -= 5
                                    self.add_area([person.x, person.y])

                if direction == 2:
                    if self.world.check_place(person.x + 5, person.y):
                        person.x += 5
                        self.add_area([person.x, person.y])

                    else:
                        if self.world.exists(person.x + 5, person.y):
                            if not self.world.check_place(person.x + 5, person.y):
                                if person.fight(self.world.get_person(person.x + 5, person.y)):
                                    person.x += 5
                                    self.add_area([person.x, person.y])

                if direction == 3:
                    if self.world.check_place(person.x, person.y - 5):
                        person.y -= 5
                        self.add_area([person.x, person.y])

                    else:
                        if self.world.exists(person.x, person.y - 5):
                            if not self.world.check_place(person.x, person.y - 5):
                                if person.fight(self.world.get_person(person.x, person.y - 5)):
                                    person.y -= 5
                                    self.add_area([person.x, person.y])

                if direction == 4:
                    if self.world.check_place(person.x, person.y + 5):
                        person.y += 5
                        self.add_area([person.x, person.y])

                    else:
                        if self.world.exists(person.x, person.y + 5):
                            if not self.world.check_place(person.x, person.y + 5):
                                if person.fight(self.world.get_person(person.x, person.y + 5)):
                                    person.y += 5
                                    self.add_area([person.x, person.y])
