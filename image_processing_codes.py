### image processing python codes

import blocks

import matplotlib.pyplot as plt


from scipy import misc,ndimage
face = misc.face()     #create the face array

#ue different smoothing filters
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)#Results
very_blurred = ndimage.gaussian_filter(face, sigma=15)
#Results
plt.imshow(<image to be displayed>)
