import numpy as np
import cv2
import matplotlib.pyplot as plt

# read image through command line
img = cv2.imread("./test_image/IMG_8609.JPG")
h, w = int(img.shape[0]), int(img.shape[1])
print(type(h),w)
img = img[900:3600,400:2400]
img = cv2.resize(img, (w//4,h//4))
plt.imshow(img)
plt.show()

# convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert the grayscale image to binary image
ret,thresh = cv2.threshold(gray_image,150,255,0)
thresh = cv2.dilate(thresh, (1,1), iterations=1)
# thresh = cv2.Canny(gray_image, 30, 200)
plt.imshow(thresh)
plt.show()

# find contours in the binary image
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

for c in contours:
     # calculate moments for each contour
    (x,y,w,h) = cv2.boundingRect(c)
    print(x,y,w,h)

    # calculate x,y coordinate of center
    if x > 0 and w > 30:
        try:
            cv2.rectangle(img, (x,y),(x+w, y+h), (0,255,0), 2)
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
            cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        except:
            continue
    

        # display the image
        cv2.imshow("Image", img)
        cv2.waitKey(0)