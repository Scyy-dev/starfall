from microbit import *

player_x = 2

display.clear()

while True:

    if button_a.was_pressed() and player_x > 0:
        player_x -= 1

    if button_b.was_pressed() and player_x < 4:
        player_x += 1

    display.clear()
    display.set_pixel(player_x, 4, 5)

    sleep(300)
