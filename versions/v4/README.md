# Objective
The objective for this version is to make the falling stars fancier and add better support for more stars.

# Line-by-line Explanation

### More Stars

First up, we'll ensure we have more stars to add to the challenge. For those that attempted the challenge in v2, this will look very familiar!

```py
stars_x = [0, 0, 0]
```

### Better Ways to Manage Stars

Up until now we've been manually adding more lines every time we add more stars. But imagine if we added 4 of 5 stars! Although, 5 stars wouldn't be very fair.

Either way, each time we add more stars, we have to add more lines. Instead, we should look at making that easier for us.

First up is when we move all the stars up to the top, their position is randomised. Instead of having to do that for all of our stars, we can just do this instead:

```py
stars_x = [random.randint(0, 4) for star in stars_x]
```

Instead of manually doing each star, this fancy statement causes the list to be regenerated with random values. For those curious, it's called a list comprehension, and it's a really cool feature in Python. We could have 100 stars, and they'll all be given a random value between 0 and 4.

The next step is to look at making displaying each of the stars easier. Currently, we display each star 1 by 1. This time however, we can't just update the list. We'll need to figure out a different way to loop over our stars.

We can replace all lines that display our stars (not our player though!) with this:

```py
for star in stars_x:
    display.set_pixel(star, star_y, 9)
```

This means that we could have 100 stars, and they'll all be displayed.

### Making our stars fancy

When we think of a falling star, we always see a trail behind it. So we're going to add that trail.

For us to add a trail, we need to think about what a trail would look like. For us, this would have some darker pixels falling above the star. It would look something like:

```
.
.
#
```

For us to achieve that, we'd need to try and show more pixels every time we draw the star. The first time, we need a pixel 1 above the current star. The next part would need a pixel 2 above the current star.

Inside the for loop where we display the stars, after we display the first star, we can add this:

```py
if star_y > 0:
    display.set_pixel(star, star_y - 1, 3)
if star_y > 1:
    display.set_pixel(star, star_y - 2, 1)
```

This first checks if the star is not at the top (we can't show a pixel out of bounds!), and then shows a pixel 1 above the star. We then do the same again, but this time 2 above the current star. (Again, gotta check if it would be out of bounds first!)

# Next Version

Great! We've made it so much easier to add more stars, and we no longer need to add lines each time we add stars. We've also added a cool trail effect behind the stars as well. You can see the full code [here](./v4.py)

The next version will be a tough one! We're going to tackle having the stars be unique to each other, and get them to not all be on the same y coordinate. You can access the next version [here](../v5/README.md)