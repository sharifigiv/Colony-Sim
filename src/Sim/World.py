class World:
    def __init__(self):
        self.all_people = []

    def new_people(self, Person):
        self.all_people.append(Person)
        
    def check_place(self, x, y):
        for p in self.all_people:
            if p.x == x and p.y == y:
                return False 

        return True

    def get_person(self, x, y):
        for p in self.all_people:
            if p.x == x and p.y == y:
                return p