def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal():
    print("Game Over")
while not at_goal():
    while wall_in_front():
        if wall_on_right():
            turn_left()
        else: 
            turn_right()
            
    while not wall_in_front():
        if wall_on_right():
            move()
        else:
            turn_right()
            move()
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    while not wall_on_right():
            turn_right()
            move()