# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:58:42 2020

@author: USER
"""

#This is a simple python program that can detect faces in an image
#The face detection accuracy can be adjusted by changing the face_off values
#To input an image, add the image to the picture folder and input the name of the image

#import neccesary library
import cv2

face_off=1.05
#add cascade file for image detection
cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image_name=""
while True:
    try:
        image_name=input("Input your image name.\nMake sure the image is in the pc picture folder")
        image=cv2.imread("C:\\Users\\USER\\Pictures\\"+image_name+".jpg")
        if image.data==None:
            sum=image+3  #this part is really just meant to give an error if that condition is met
    except:
        try:
            image=cv2.imread("C:\\Users\\USER\\Pictures\\"+image_name+".png")
            if image.data==None:
                sum=image+3   #this part is really just meant to give an error if that condition is met
        except:
            print("This image does not exit.\nMake sure the file is a jpg or png image and that it is in your PC's picture folder")
        else:
            break
    else:
        break
    
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
positions=cascade.detectMultiScale(grey_image, scaleFactor=face_off, minNeighbors=5)
for x,y,w,h in positions:
    image=cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
cv2.imshow("Face Detector",image) #shows image with rectangle detecting faces in it
cv2.waitKey(0)               
       
