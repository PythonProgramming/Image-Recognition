'''
Hello and welcome to image recognition tutorial series. This series will just
be a simple introduction to the field.

to start this series, you will need 4 things:

Python (get 64 bit if you have 64bit windows.)

PIL (python imaging library)
If you have 64-bit python, you will need to get Pillow instead:
Even if you have 32-bit python, you can also download pillow.

http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow

Numpy.
http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy


matplotlib:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib


Make sure you match your python bit version to
whatever you download.



'''


#############
#import Image
# ... if you decide to not download pillow, and want to use PIL, then you
# will import image. Otherwise, do:
#############

from PIL import Image
import numpy as np

i = Image.open('images/dot.png')

iar = np.asarray(i)

'''
Alright, so an image array comes out as a 3-dimensional array. This means an
array within an array an array, or list. So the entire list is the whole image.
The 2nd dimension in,
corresponds to the row, and the 3rd dimension in
corresponds to each pixil in that row.. or u can
think of it like a column.

within the pixil arrays, you have your typical Red Green Blue, or RGB, and then you
are also supplied with an "alpha"... and this is for each pixil.

So that's just a quick example. In the next example, we'll be breaking things
down further, and beginning to build some recognition.

'''
print(iar)
