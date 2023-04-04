
# author @Farhanugraha 
# import library opencv
import cv2 as cv

filepath = 'data//landscape.jpg'
contimage = cv.imread(filepath,cv.IMREAD_COLOR)
size = (100,100)

# display image without resizing
cv.imshow("image",contimage)
cv.waitKey(0)

imageresize = cv.resize(contimage,size,cv.INTER_AREA)
cv.imshow("resize image",imageresize)
cv.waitKey(0)

# grayscale
graycolor = cv.cvtColor(imageresize,cv.COLOR_BGR2GRAY)

cv.imshow("resize image with gray",graycolor)
cv.waitKey(0)


output = 'data\\save_image.png'
cv.imwrite(output,contimage)
print("Alert!! picture has been saved {}".format(output))