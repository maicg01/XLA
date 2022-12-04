import cv2
import numpy as np
import matplotlib.pyplot as plt
 
 
planets	= cv2.imread("./test_image/IMG_8615.JPG")
planets = planets[900:3600,400:2400]
h, w = int(planets.shape[0]), int(planets.shape[1])
planets = cv2.resize(planets, (w//4,h//4))
gray_img = cv2.cvtColor(planets,cv2.COLOR_BGR2GRAY)
img	= cv2.medianBlur(gray_img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
plt.imshow(cimg)
plt.show()
 
#center
 
circles	= cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)
circles	= np.uint16(np.around(circles))
 
for	i in circles[0,:]:
				#	draw	the	outer	circle
				cv2.circle(planets,(i[0],i[1]),i[2],(0,255,0),2)
				#	draw	the	center	of	the	circle
				cv2.circle(planets,(i[0],i[1]),2,(0,0,255),3)
 
cv2.imshow("HoughCirlces",	planets)
cv2.waitKey(0)
cv2.destroyAllWindows()