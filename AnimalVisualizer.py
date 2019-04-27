import glob
import numpy as np
import cv2
import csv


	
file='annotations.npy'
a=np.load(file)

img=cv2.imread(a[0][0])
cv2.namedWindow('zebra')
cv2.imshow('zebra',img)	
img=cv2.resize(img,(1280,720))
cv2.imshow('zebra',img)
curr=a[0]

cv2.waitKey(0)

cv2.destroyAllWindows()
	


cv2.line(img,curr[1],curr[2],(255,255,0),10)
cv2.line(img,curr[2],curr[3],(255,255,0),10)
cv2.line(img,curr[3],curr[4],(255,255,0),10)
cv2.line(img,curr[4],curr[5],(255,255,0),10)

cv2.line(img,curr[6],curr[7],(255,255,0),10)
cv2.line(img,curr[7],curr[8],(255,255,0),10)

cv2.line(img,curr[9],curr[10],(255,255,0),10)
cv2.line(img,curr[10],curr[11],(255,255,0),10)

cv2.line(img,curr[12],curr[13],(255,255,0),10)
cv2.line(img,curr[13],curr[14],(255,255,0),10)

cv2.line(img,curr[15],curr[16],(255,255,0),10)
cv2.line(img,curr[16],curr[17],(255,255,0),10)

cv2.line(img,curr[18],curr[19],(255,255,0),10)
cv2.line(img,curr[20],curr[21],(255,255,0),10)


for i in range(1,len(a[0])):
	cv2.circle(img,(curr[i][0],curr[i][1]),5,(0,0,255),10)


cv2.imshow('zebra',img)

cv2.waitKey(0)

cv2.destroyAllWindows()

black=np.zeros((720,1280,3),np.uint8)
img=black
cv2.line(img,curr[1],curr[2],(255,255,0),10)
cv2.line(img,curr[2],curr[3],(255,255,0),10)
cv2.line(img,curr[3],curr[4],(255,255,0),10)
cv2.line(img,curr[4],curr[5],(255,255,0),10)

cv2.line(img,curr[6],curr[7],(255,255,0),10)
cv2.line(img,curr[7],curr[8],(255,255,0),10)

cv2.line(img,curr[9],curr[10],(255,255,0),10)
cv2.line(img,curr[10],curr[11],(255,255,0),10)

cv2.line(img,curr[12],curr[13],(255,255,0),10)
cv2.line(img,curr[13],curr[14],(255,255,0),10)

cv2.line(img,curr[15],curr[16],(255,255,0),10)
cv2.line(img,curr[16],curr[17],(255,255,0),10)

cv2.line(img,curr[18],curr[19],(255,255,0),10)
cv2.line(img,curr[20],curr[21],(255,255,0),10)


for i in range(1,len(a[0])):
	cv2.circle(img,(curr[i][0],curr[i][1]),5,(0,0,255),10)

cv2.imshow('zebra',black)

cv2.waitKey(0)

cv2.destroyAllWindows()




