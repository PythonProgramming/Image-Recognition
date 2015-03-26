'''
So let's read some of our numbers now.

Let's take zero for example.

Even the exact same zero, we can see that it can make a big difference in the
numbers when we change the background

then when we change the color of the zero itself

... so then what do we do in these situations?

Typically, OCRs, or optical character recognizers dont look @ at colors
like humans would. So, if you have two colors very similar to eachother,

the computer is less likely to have issue with it.
This is because the computer is looking at numbers only.

Instead, the computers
have more issue with "fuzz" so to speak, or blurry edges. The computer
wants to see clear differences and edges. Lack of that is what makes it
hard to read. The other thing that can hurt is overlapping letters,
or modifying their shape. If you've ever seen a captcha, that's basically
it... lines thru the letters, deforming the letters... etc.

combatting blur is pretty simple, by thresholding the image.

I will show that first. 

'''

from PIL import Image
import numpy as np
####
import matplotlib.pyplot as plt
###
i = Image.open('images/numbers/y0.5.png')

iar = np.asarray(i)


plt.imshow(iar)
print(iar)
plt.show()





