from microbit import *
import random

player_x = 0

stars = [[4, 3], [3, 2], [4, 1], [3, 0]]

presses_a = 0
presses_b = 0

score = 0 - len(stars)
speed = 300

display.clear()

game_over = False
while True:

    if button_a.was_pressed() and player_x > 0:
        player_x -= 1

    if button_b.was_pressed() and player_x < 4:
        player_x += 1

    for star in stars:
        star[1] += 1
        if star[1] > 4:

            if player_x == star[0]:
                game_over = True
                break

            star[0] = random.randint(0, 4)
            star[1] = 0

            score += 1
            if speed > 100:
                speed -= 1

    if game_over:
        break

    display.clear()
    display.set_pixel(player_x, 4, 5)
    for star in stars:
        star_x = star[0]
        star_y = star[1]
        display.set_pixel(star_x, star_y, 9)
        if star_y > 0:
            display.set_pixel(star_x, star_y - 1, 3)
        if star_y > 1:
            display.set_pixel(star_x, star_y - 2, 1)

    sleep(speed)


display.scroll("Score " + str(score))
