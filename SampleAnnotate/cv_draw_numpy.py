import glob
import numpy as np
import cv2
import csv

filenames=glob.glob("*.jpg")

largeArray=[]

nfile='annotations.npy'
parts=['nose','head','neck','tail','tailEnd','FrontLeftA','FrontLeftB','FrontLeftC','FrontRightA','FrontRightB','FrontRightC','RearLeftA','RearLeftB','RearLeftC','RearRightA','RearRightB','RearRightC','LeftEarA','LeftEarB','RightEarA','RightEarc']


def onMouse(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDOWN:
		output.append((x,y))
		cv2.circle(img,(x,y),5,(0,0,255),10)
		cv2.waitKey(1)
		cv2.imshow('zebra',img)
	
	if event==cv2.EVENT_MBUTTONDOWN:
		arr.append((x,y))
	if event==cv2.EVENT_MBUTTONUP:
		cv2.line(img,arr.pop(),(x,y),(255,255,0),10)
		cv2.waitKey(1)
		cv2.imshow('zebra',img)





for file in filenames:
	cv2.namedWindow('zebra')
	img=cv2.imread(file)
	img=cv2.resize(img,(1280,720))
	output=[]
	output.append(file)
	arr=[]
	cv2.imshow('zebra',img)
	cv2.setMouseCallback('zebra',onMouse)
	cv2.waitKey(0)
	cv2.imwrite("annotated/"+file,img)
	cv2.destroyAllWindows()
	print(output)
	largeArray.append(output)

out_np=np.array(largeArray)
np.save(nfile,out_np)


	






