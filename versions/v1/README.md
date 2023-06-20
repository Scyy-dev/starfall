# Objective
The objective for this version is to add basic player movement on the Micro:bit. We are not worried about adding the stars, score, a way to lose or any fancy effects yet.

# Line-by-line Explanation

### Important Libraries

```py
from microbit import *
```

This line tells the Micro:Bit to use a special set of tools (called "libraries") we need. Without it, we can't control the Micro:Bit!

### Player Data

```py
player_x = 2

presses_a = 0
presses_b = 0
```

This line sets the starting position of the player (represented by a pixel). We'll use the `presses_a` and `presses_b` variables later on - we use them to help us control the player!

### Showing Our Player

```py
display.clear()
display.set_pixel(player_x, 4, 5)
```

This line makes the Micro:bit show our player! The player_x variable can be changed to move our player. The Micro:bit uses a coordinate and brightness system to control the LEDs. You can read about how they work at [The Micro:bit Reference](https://microbit-micropython.readthedocs.io/en/latest/display.html)

### Starting Our Game Loop

```py
while True:
```

This line starts an infinite loop. We'll see how it's useful in just a moment.

### Controlling our player

This bit is a little tricky, so we'll break it down after writing it out. Make sure it's inside the infinite loop!

```py
if presses_a is not button_a.get_presses() and player_x > 0:
    player_x -= 1
    presses_a = button_a.get_presses()
```

The first line here is a big if statement that does multiple things. It first checks to see if the number of times the player has pressed the 'A' button matches with the number stored on the Micro:bit. If they don't match, it means the player has pressed the button!

We also don't want the player to move outside the display screen. So we check to see if they're already at the edge first.

Once we know that they've pressed the button AND that they're not on the edge, we move the player to the left. We also update our button press count for the next time they press the button.

Now we repeat this for the 'B' button, again making sure it's inside our forever loop:

```py
if presses_b is not button_b.get_presses() and player_x < 4:
    player_x += 1
    presses_b = button_b.get_presses()
```

Great! We've added the ability to move left and right. But the display isn't updating, so we need to move the display call to inside the infinite loop as well.

### Giving the game time

The only issue now is that we don't get to see the player anymore! Or if we do, it flickers for a split second and then disappears again.

This is because the display is being cleared faster than it can display the player! To fix this, we need to slow it all down. We add this bit of code after we display the player so we get time to see our player:

```py
sleep(300)
```

I chose 300 milliseconds because it sets a good pace for our game. We'll see in later versions why the number we put there is important.

### Final Cleanup

If you've noticed that the display sometimes doesn't fully reset between uses, you can add this before your infinite loop to fix it:

```py
display.clear()
```

This ensures that there is nothing being displayed before our game starts.

And that's everything! We've added our player and given them the power to move left and right. We'll be adding something to dodge in [v2](../v2/README.md).

You can also see the completed version [here](./v1.py).

