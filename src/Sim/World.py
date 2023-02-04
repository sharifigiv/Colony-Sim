class World:
    def __init__(self, x, y, width, height):
        self.all_people = []

        self.x = x
        self.y = y

        self.width = width
        self.height = height

    def new_people(self, Person):
        self.all_people.append(Person)
        
    def check_place(self, x, y):
        if x >= self.x and x <= self.width + self.x and y >= self.y and y <= self.height + self.y:
            for p in self.all_people:
                if p.x == x and p.y == y:
                    return False 

            return True

        else:
            return False

    def get_person(self, x, y):
        for p in self.all_people:
            if p.x == x and p.y == y:
                return p