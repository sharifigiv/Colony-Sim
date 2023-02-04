from Sim import World, Colony, Human
import pyray as pr 
import time
from random import choice

pr.init_window(1080, 720, 'Colony Simulator')

w = World.World(0, 0, 500, 500)
w.colonies.append(Colony.Colony('meymanat', pr.YELLOW, pr.Color(253, 249, 0, 150), w))
w.colonies.append(Colony.Colony('Azaz', pr.RED, pr.Color(230, 41, 55, 150), w))

old_time = time.time()

while not pr.window_should_close():
    new_time = time.time()

    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    if pr.is_mouse_button_pressed(0):
        colon = choice(w.colonies)
        x, y = w.random_pos()

        x -= x % 5
        y -= y % 5
        
        Person = Human.Human(x, y, 90, False, colon)
        colon.add_people(Person)

    if round(new_time - old_time, 2) >= 0.01:        
        for colony in w.colonies:     
            colony.update()

        old_time = new_time

    for colony in w.colonies:
        for p in colony.people:
            pr.draw_rectangle(p.x, p.y, 5, 5, colony.color)

        for block in colony.area:
            pr.draw_rectangle(block[0], block[1], 5, 5, colony.area_color)
                
    pr.end_drawing()