# @author Farhan Nugraha
# Convolutin image with Object Oriented Programming
import numpy as np
import cv2

class ImageConvolution:
    def __init__(self, image):
        self.image = image

    # function to sharpening image
    def sharpening(self):
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1], 
                           [0, -1, 0]])
         # using method filter2D()
        return cv2.filter2D(self.image, -1, kernel)
    # function to deblurring image
    def deblurring(self):
        kernel = np.array([[1/9, 1/9, 1/9],
                           [1/9, 1/9, 1/9],
                           [1/9, 1/9, 1/9]])
        # using method filter2D()
        return cv2.filter2D(self.image, -1, kernel)
    # function to sobel edge detection
    def sobel_edge_detection(self):
        sobel_x = np.array([[-1, 0, 1],
                            [-2, 0, 2],
                            [-1, 0, 1]])
        
        sobel_y = np.array([[-1, -2, -1],
                            [0, 0, 0],
                            [1, 2, 1]])
         # using method filter2D()
        img_x = cv2.filter2D(self.image, -1, sobel_x)
        img_y = cv2.filter2D(self.image, -1, sobel_y)
        return cv2.addWeighted(img_x, 0.5, img_y, 0.5, 0)

filepath = 'lenna.jpg'
# input image with greyscale
image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
img_conv = ImageConvolution(image)
sharpened_img = img_conv.sharpening()
deblurred_img = img_conv.deblurring()
sobel_img = img_conv.sobel_edge_detection()

# output image
cv2.imwrite("img_conv.jpg", img_conv)
cv2.waitKey(0)
cv2.imwrite("sharpened.jpg", sharpened_img)
cv2.waitKey(0)
cv2.imwrite("deblurred.jpg", deblurred_img)
cv2.waitKey(0)
cv2.imwrite("sobel.jpg", sobel_img)
cv2.waitKey(0)
