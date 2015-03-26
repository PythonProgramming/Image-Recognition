'''
Now, as we begin working, it will be useful for us to visualize
what we're doing.

As time goes on, we'll be using some basic skills to

"simplify" images and make them easier for us to read.

To make sure that we're doing that right, and to
actually see what the program is seeing besides reading the arrays
and acting like we're in the matrix movies and can just instantly
see it... it might be helpful to plot it up.

Luckily, doing this is super easy with matplotlib.

'''

from PIL import Image
import numpy as np
####
import matplotlib.pyplot as plt
###
i = Image.open('images/dot.png')

iar = np.asarray(i)


plt.imshow(iar)
print(iar)
plt.show()





