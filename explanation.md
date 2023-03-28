## Game Concept
This code is for a simple game on the Micro:Bit where players have to avoid falling stars by moving left or right using the A and B buttons. The game starts with the player (represented by a pixel) located at the bottom center of the Micro:Bit display. Stars will begin falling randomly from the top of the display and the player must move the character left or right to avoid colliding with the falling stars.

The player moves left by pressing button A and right by pressing button B. Each time the player avoids colliding with a falling star, their score increases by one. The game ends when the player collides with a falling star, and their final score is displayed on the Micro:Bit display. Players can play again by pressing the 'reset' button on the back of the Micro:Bit

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

## Explanation Notes
A significant portion of this explanation was generated with assistance from [ChatGPT](https://openai.com/blog/chatgpt). It is highly recommended to use this tool to assist with the explanation process if you are unable to explain a concept through a particular lens (e.g. primary/high school students).

This game was designed with simplicity in mind - certain features (e.g. fancier stars, lives, particle effects on collision/loss, etc) were intentionally culled in favour of keeping the code simple and easy to explain.
