# Objective
This version will make each of the stars unique, and not attached to the same y coordinate. It will be a step up in difficulty compared to the previous versions.

# Line-by-line Explanation

### Making our Stars Independent

This first bit will give us the structure for our stars to be independent. It will break most of our other code, but that's okay, we'll be going through and fixing up every issue we encounter till we can get it working.

For our stars to be unique they must maintain their own version of the y coordinate, it must no longer be shared between each of the stars.

The simplest way to implement this is to create a list of lists! our stars list will be a list of lists, and the lists it contains will contain the x and y coordinate of our stars. Bit confused? It gets worse before it gets better!

We can do this with the following code. Make sure to get rid of the `stars_x` *and* `star_y` variables before doing this:

```py
stars = [[4, 3], [3, 2], [4, 1], [3, 0]]
```

We intentionally create all of our stars staggered, as this ensures that they won't all descend at the same y coordinate.

### Fixing the Initial Score

The first impact we encounter in our code is how we score. Previously, we would give a score every time all the stars got reset. But since they're all independent, we're now giving score every time a single star moves up top.

This means we need to change what we did earlier with the score adjustment. Before, it was just 1 point for all stars. But now it's one point per star, so we need to change the adjustment to suit the number of stars.

We change the initial score like so:

```py
score = 0 - len(stars)
```

This ensures that regardless of the number of stars we add, we will always start with the right amount of score.

### A Better Way to Loop

our infinite loop will be affected by fixes we do later, but it's better to fix it now. so instead, we'll change it so it's easier to escape from that loop. We'll add a simple check for if we escape from the loop, and we'll be using it later:

Make sure to add this just before the infinite loop:

```py
game_over = False
```

### Player Input

Because we've only changed the way stars are handled, we don't need to change the way our player input is handled.

### Star Logic

We have to change the way we handle the stars now. We need to apply the logic to every star at any time, not just when all stars hit y4.

To go about this, we just have to wrap our star logic in a for loop that loops over each of our stars. Each time we operate on `stars_x` we'll do it inside the for loop using `star[0]`, and every reference to `star_y` will get replaced with `star[1]`.

We'll also need to add a bit for the game_over part we added earlier, because `break` will only take us out of the for loop.

The speed is also impacted by this change. Instead of reducing the speed by 5 when all stars fire, we can instead reduce it by 1 every time a star is reset.

It can be a bit confusing for everything going on, so the following code applies all changes at once:

```py
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
```

That's a lot to take in! Don't worry if you got stuck on a few things, there was a lot going on. That's most the hard work handled for us though! Congrats if you managed to get it all in one attempt.

### Fixing Star Displays

Now to move onto displaying the stars. What we have already is very easy to work with, we just need make a few tweaks to get everything working as intended.

for this bit, we need to replace the for loop we have already with one that uses the new `stars` variable instead of the old `stars_x`. We'll also need to replace every reference to the old `star` with `star_x`. And finally, at the start of the loop, we need to help our old code understand the new stuff, by linking the old `star_x` and `star_y` to our new code.

It'll be a challenge to get all this stuff working in one shot. And that's okay! Give it a go and see how far you get!

It's important that the display clearing and player display stuff isn't touched, as otherwise our player won't display correctly.

```py
for star in stars:
    star_x = star[0]
    star_y = star[1]
    display.set_pixel(star_x, star_y, 9)
    if star_y > 0:
        display.set_pixel(star_x, star_y - 1, 3)
    if star_y > 1:
        display.set_pixel(star_x, star_y - 2, 1)
```

### Further Challenges

Great job for making it this far! If you've managed to get everything working up to this point, you should have a fun, challenging game with some interesting visuals. If you got stuck, you can see the full code [here](./v5.py)

If you want to challenge yourself further, I recommend trying to add the following features:
* Add a lives system so players get lives
* Make the player flash after being hit
* Add some more text or a better game over screen
