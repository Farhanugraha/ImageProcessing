import cv2 as cv

filetemp = 'data//lenna.jpg'
contimage = cv.imread(filetemp,cv.IMREAD_COLOR)


imagevertikal = cv.flip(contimage,0)
imagehorizontal = cv.flip(contimage,1)
imageboth = cv.flip(contimage,-1)

cv.imshow("original",contimage)
cv.waitKey(0)

cv.imshow("vertikal",imagevertikal)
cv.waitKey(0)

cv.imshow('horizontal',imagehorizontal)
cv.waitKey(0)

cv.imshow('both',imageboth)
cv.waitKey(0)

