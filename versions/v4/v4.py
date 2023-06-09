from microbit import *
import random

player_x = 2

stars_x = [0, 0, 0]
star_y = 4

presses_a = 0
presses_b = 0

score = -1
speed = 300

display.clear()

while True:

    if button_a.was_pressed() and player_x > 0:
        player_x -= 1

    if button_b.was_pressed() and player_x < 4:
        player_x += 1

    star_y += 1

    if star_y > 4:
        if player_x in stars_x:
            break
            
        stars_x = [random.randint(0, 4) for star in stars_x]
        star_y = 0

        score += 1
        if speed > 100:
            speed -= 5

    display.clear()
    display.set_pixel(player_x, 4, 5)
    for star in stars_x:
        display.set_pixel(star, star_y, 9)
        if star_y > 0:
            display.set_pixel(star, star_y - 1, 3)
        if star_y > 1:
            display.set_pixel(star, star_y - 2, 1)

    sleep(speed)


display.scroll("Score " + str(score))