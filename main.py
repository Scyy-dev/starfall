from microbit import *
import random

player_x = 2
player_y = 4

stars = [0, 0]
star_y = 4

presses_a = 0
presses_b = 0

score = 0
speed = 300

display.clear()

while True:

    if presses_a is not button_a.get_presses() and player_x > 0:
        player_x -= 1
        presses_a = button_a.get_presses()
    if presses_b is not button_b.get_presses() and player_x < 4:
        player_x += 1
        presses_b = button_b.get_presses()
        
    star_y += 1
    if star_y > 4:
        if player_x in stars:
            break
        
        stars[0], stars[1] = (random.randint(0, 4), random.randint(0, 4))
        star_y = 0
        score += 1
        if speed > 100:
            speed -= 5
    
    display.clear()
    display.set_pixel(player_x, 4, 5)
    display.set_pixel(stars[0], star_y, 9)
    display.set_pixel(stars[1], star_y, 9)
    
    sleep(speed)
    
    
display.scroll("Score " + str(score))