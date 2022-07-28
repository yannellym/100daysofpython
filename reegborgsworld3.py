def turn_around():
    turn_left()
    turn_left()
    turn_left()

def one_jump():
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()
 
    
while not at_goal():
   if not wall_in_front() or front_is_clear():
    move()
   else:
    one_jump()
      
