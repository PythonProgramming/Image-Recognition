'''
Alright, so dot.png is an 8x8 pixil image,

As we can see, it's just a single dot. so when we bring it up:

'''


from PIL import Image
import numpy as np
###
i = Image.open('images/dotndot.png')

iar = np.asarray(i)

print(iar)


'''
we can see how the first pixil has an RGB of 0, 0, 0, then an alpha of 255.
This means we have a solid color, which is solid black, or lack of any color.

All other pixils have 255,255,255 rgb... which makes sense since white
contains all colors in the visible spectrum.

The next question that usually comes up is... why rbg and not ryb??

Weren't we all taught in art that the 3 primary colors that made
all the other colors were Red Yellow and Blue?..

so why are we using red greed blue?

this boils down to additive colors vs subtractive colors.

Additive colors add light as you stack them up. So if you just have a little bit
of red, it is somewhat dull and dark. If you have a LOT of red, it creates
a bright red.

This is the opposite for subtractive colors. So when you say paint some
red... then paint some more red over the previous red... it becomes darker.

Since, with computers, we are working with monitors, they are emitting light,
so it just makes sense to consider it additive coloring. 


The more you know.

So let's add a green dot to our file.... check the RGB in paint, and run again.

so that's that, hopefully you now understand the translation of colors to
numbers, and those numbers into the 3d array. 
'''


