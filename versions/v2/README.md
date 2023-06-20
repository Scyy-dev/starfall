# Objective
The objective for this version is to add some stars that can fall above the player. We won't be adding a score, effects or a way for the player to lose.

# Line-by-line Explanation

### Important Libraries

```py
import random
```

Before we can begin, we'll need another library - the random library. This library lets us generate random numbers, which we need so our game isn't predictable or boring. Make sure to put this one with the other libraries!

### Star Data

We need to track where our stars are at every moment. To do this, we hold a list of the x coordinate of each star, and assume they all have the same y coordinate. (We give them unique coordinates in [v5](../v5/README.md)!)

```py
stars_x = [0]
star_y = 4
```

We'll start with 1 star for now. You'll note that the stars start at y4. This is intentional, and we'll get to see that when we change the main loop.

### Show the Stars

Now that we have our stars, we need to make them show up on the display.

```py
display.set_pixel(stars_x[0], star_y, 9)
```

We want our stars to be bright so we set them to be the maximum brightness, and their coordinates are taken from the star coordinates. But our stars don't move!

### Moving the Stars

The logic behind moving the stars is a little tricky. To get our stars to move, we need to update their y coordinate. Once they hit the bottom, we move them back up to the top.

To do this, we need to increase their y coordinate every time inside the infinite loop. We'll then need to check if they've reached the bottom (y4), and teleport them up to the top (y0). We need to make sure this bit of code runs before we update the display, but before our player provides input. This ensures the stars are updated before we try to display them.

```py
star_y += 1
if star_y > 4:
    stars_x[0] = random.randint(0, 4)
    star_y = 0
```

The first line is resonsible for actually moving the stars. Every time the loop runs, the stars will move down a pixel. The if statement checks if they've hit the bottom.

The next line is the fun part. While moving them to the top, we randomize where they'll reappear up top, using the random library we imported earlier. Finally, the part that actually moves them to the top is the last line. It changes the y level for all stars to be up top.

Great! We now have a star moving around.

### Challenge

Now that we have 1 star moving, why not try add a second star? I'll give you a hint to get started: You'll need to change

```py
stars_x = [0]
```

to

```py
stars_x = [0, 0]
```

There are multiple ways to go about adding another star, but this approach is a good approach to make it easier to add even more stars in future as well.

# Next Version

Great! We now have a player that can move, and a star (or multiple stars!) that can fall. If you got stuck adding another star, you can see the full code [here](./v2.py).

The next version will add a scoring system, so we can tell how many times the player avoided the stars! We'll also look at a way to make it harder the longer we play. You can access the next version [here](../v3/README.md)
