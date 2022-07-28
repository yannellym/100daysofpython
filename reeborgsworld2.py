def turn_around():
    turn_left()
    turn_left()
    turn_left()

def one_jump():
    move()
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()

while not at_goal():
   one_jump()
