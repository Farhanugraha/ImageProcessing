import cv2 as cv
import numpy as np

containerimage = "data//lenna.jpg"
image = cv.imread(containerimage,cv.IMREAD_COLOR)
image = cv.resize(image, (512,512))

# original image
cv.imshow("original",image)
cv.waitKey(0)

# horizontal image
horizontalimage = image[:, ::-1]
cv.imshow("horizontal",horizontalimage)
cv.waitKey(0)

# vertikal image
vertikalflip = image[::-1]
cv.imshow("vertikal",vertikalflip)
cv.waitKey(0)

# rgb image with flip
rgb = image[:, :, ::-1]
cv.imshow("rgb",rgb)
cv.waitKey(0)



