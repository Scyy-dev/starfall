# Objective
The objective for this version is to add a scoring system, a way to lose, and a way for the game to get harder over time.

# Line-by-line Explanation

### Score and Speed

To make the game harder, we'll make the stars fall faster the longer we keep playing. To do this, we'll need to know what the current 'speed' is. We also want to track the current score, which will be a count for the number of times the player has survived the stars.

```py
score = 0
speed = 300
```

For the speed we set to take effect, we'll also need to change the value used by the `sleep()` call, as shown:

```py
sleep(speed)
```

### A Way to Lose

First up, before we try and get the score and speed working, we need a way for the player to lose. Currently, they can be hit by as many stars as they like!

To fix this, we need to check if a player *collides* with the stars. We have a handy way to check this. Because the only time the player can collide with the stars is when the star is at the bottom (y4). We also know where all the stars are (`stars_x), so we just need to compare the player_x with the stars_x!

Inside of our `star_y > 4` check, we can add the following:

```py
if player_x in stars_x:
    break
```

This checks if the playes is currently colliding with a star, and if they are, ends our infinite loop!

### A Losing Message

Now that we've got a way to lose, we need to tell the player that they lost. The easiest way to go about this is to tell the player their score!

at the end of our code, outside of our infinite loop, we can add the following text display:

```py
display.scroll("Score " + str(score))
```

This will print out the score the player achieved.

### Increasing our Score

Now it's time to tackle the problem where our players get stuck at 0 score all the time. To fix this, we need a way to give them a score.

The way we tackle this is by giving them a score every time the stars move up to the top. This means the player has survived a 'round' of stars, and we increase the score by 1.

Inside of our `star_y > 4` check, we can add the following:

```py
score += 1
```

This adds one to our score. It's import that this is written *after* the star collision check, as otherwise the player will get a free score, even if they've collided with a star.

### Making the Game Harder

We've got one more thing to do - make the game harder as time goes on. The way we go about this is to make the stars fall faster. We can do this by reducing the time we pause the game at the end of the loop.

We could simply change the speed to be something smaller, but that doesn't let us change it over time. Instead, we should make it harder every time the player earns score. We can do this by adding the following bit of code after we increase the score:

```py
if speed > 100:
    speed -= 5
```

This first checks to see if our speed is above 100 - If it was below 100, that might be too fast for us to handle! We want to make it a challenge, not impossible.

The next line reduces the speed by 5. I chose this number because it sets a good pace for the game, slow start but it ramps up quick.

### Finishing Touches

There's a small issue that occurs if we get hit straight away - we get a score of 1! That doesn't make any sense, because we haven't survived any stars yet. To fix this, we just need to set the starting score to -1:

```py
score = -1
```

This is needed because our stars actually start at the bottom, and then get moved to the top, causing the player to earn a score for free. The -1 starting score fixes that problem.

# Next Version

Great! We've got a playable game - a player that can move, stars to dodge, a score, and it gets harder the longer we play. You can see the full code [here](./v3.py)

The next version will look at some code clean-up and adding some fancy effects for the stars, which can be accessed [here](../v4/README.md)
