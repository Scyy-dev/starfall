# Game Concept
This code is for a simple game on the Micro:Bit where players have to avoid falling stars by moving left or right using the A and B buttons. The game starts with the player (represented by a pixel) located at the bottom center of the Micro:Bit display. Stars will begin falling randomly from the top of the display and the player must move the character left or right to avoid colliding with the falling stars.

The player moves left by pressing button A and right by pressing button B. Each time the player avoids colliding with a falling star, their score increases by one. The game ends when the player collides with a falling star, and their final score is displayed on the Micro:Bit display. Players can play again by pressing the 'reset' button on the back of the Micro:Bit
<br><br><br>

# Code Explanation
## Libraries
```py
from microbit import *
```

This line tells the Micro:Bit to use a special set of tools (called "libraries") that help it run the code we're going to write. Without it, we can't control the Micro:Bit!

```py
import random
```

This line tells the Micro:Bit to use another special tool that helps us create random numbers. We use random numbers to make the game fun!

## Game State

```py
player_x = 2
player_y = 4
```

These lines set the starting position of the player (represented by a pixel) to be at the bottom of the Micro:Bit display.

```py
stars = [0, 0]
star_y = 4
```

These lines set the starting position of the falling stars and its y-coordinate (how far up or down it is on the Micro:Bit display).

```py
presses_a = 0
presses_b = 0
```

These lines keep track of how many times the player has pressed buttons A and B. We use this to tell when the player wants to move left or right.

```py
score = 0
speed = 300
```

These lines set the starting score of the player to zero and the starting speed of the falling stars to 300 milliseconds.

```py
display.clear()
```

This line clears the Micro:Bit display before the game starts.

## Core Game Loop
```py
while True:
```

This line starts a forever loop. This means the game will never stop until we tell it to stop.

### Player Movement

```py
if presses_a is not button_a.get_presses() and player_x > 0:
    player_x -= 1
    presses_a = button_a.get_presses()
```

These lines check if the player has pressed the A button. When the player presses the A button, the player moves to the left.

```py
if presses_b is not button_b.get_presses() and player_x < 4:
    player_x += 1
    presses_b = button_b.get_presses()
```

These lines check of the player has pressed the B button. When the player presses the B button, the player moves to the right.

### Star Movement

```py
star_y += 1
```

This moves the stars down a pixel. We use this so the stars can actually 'fall' on the display!

### Collision Check

```py
if star_y > 4:
```

Once the stars reach the bottom of the display, we need to check if the player is touching any stars.

```py
if player_x in stars:
    break
```

This checks if the players position is the same as any of the stars. If it is, Game Over! We 'break' (exit) out of the loop and show the score.

```py
stars[0], stars[1] = (random.randint(0, 4), random.randint(0, 4))
star_y = 0
```

Once our stars have hit the bottom and they aren't touching the player, we need to reset the stars. This randomly shuffles our falling stars so they're in a new position, starting again at the top.

```py
score += 1
if speed > 100:
    speed -= 5
```

Once the stars have been reset, the player has 'survived' one round of stars. So we need to give them a score, and ramp up the challenge by making the stars fall faster.

### Display

```py
display.clear()
display.set_pixel(player_x, 4, 5)
display.set_pixel(stars[0], star_y, 9)
display.set_pixel(stars[1], star_y, 9)
```

Now that our player and stars have been updated, we need to actually display the stars and the player. To do this we reset the display so it's blank, and then redraw the player and the stars.

### Game Speed

```py
sleep(speed)
```

To make sure the stars don't fall super-duper fast, we slow them down by pausing the game. How long we pause them for slowly gets smaller and smaller the longer the player is alive.

## Game Over Screen

```py
display.scroll("Score " + str(score))
```

Once the player hits a star, the game is over, and we show them the score they got.
<br><br><br>

# Explanation Notes
A significant portion of this explanation was generated with assistance from [ChatGPT](https://openai.com/blog/chatgpt). It is highly recommended to use this tool to assist with the explanation process if you are unable to explain a concept through a particular lens (e.g. primary/high school students).

This game was designed with simplicity in mind - certain features (e.g. fancier stars, lives, particle effects on collision/loss, etc) were intentionally culled in favour of keeping the code simple and easy to explain.
