from microbit import *

player_x = 2

presses_a = 0
presses_b = 0

display.clear()

while True:

    if presses_a is not button_a.get_presses() and player_x > 0:
        player_x -= 1
        presses_a = button_a.get_presses()

    if presses_b is not button_b.get_presses() and player_x < 4:
        player_x += 1
        presses_b = button_b.get_presses()

    display.clear()
    display.set_pixel(player_x, 4, 5)

    sleep(300)
