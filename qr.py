from pylab import imshow, show, get_cmap
from numpy import random

Z = random.random((50,50))   # Test data


imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
show()
# Save the image
im.save('qr.png')
