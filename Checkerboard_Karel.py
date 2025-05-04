from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""
def main():
    put_beeper()
    complete_east_line()
    return_to_start()

def complete_east_line():
    alternate_to_wall()
    turn_left()
    if front_is_clear():
        start_next_line()
        turn_left()
        complete_west_line()

def complete_west_line():
    alternate_to_wall()
    turn_right()
    if front_is_clear():
        start_next_line()
        turn_right()
        complete_east_line()

def start_next_line():
    if beepers_present():
        move()
    else:
        move()
        put_beeper()

def alternate_to_wall():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            move()
            put_beeper()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def return_to_start():
    # Face South: Karel turns around (because it ends at the top)
    turn_around()
    # Move straight down
    while front_is_clear():
        move()
    # Turn to face West (left)
    turn_right()
    # Move to far-left wall
    while front_is_clear():
        move()
    # Face East again
    turn_left()
    turn_left()

    



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
