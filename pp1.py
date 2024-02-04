#1 : Learn Opencv In 3 Hour

import cv2
import numpy as np
##1

# img = cv2.imread("img1.jpg")
# cv2.imshow("out" , img)
# cv2.waitKey(0)


##2


# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10 , 50)
# while True:
#     s , img = cap.read()
#     cv2.imshow("vid" , img)
#     if cv2.waitKey(1) & 0xFF ==ord(' '):
#         break


#3


# img = cv2.imread('i.jpg')
# imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(img , (7,7) , 0)
# imgcanny = cv2.Canny(img , 100 , 100)
# cv2.imshow("img gray" , imggray)
# cv2.imshow("img blur" , imgblur)
# cv2.imshow("img canny" , imgcanny)
# cv2.imshow("img" , img)
# cv2.waitKey()
# if 0xFF ==ord(' '):
#     cv2.destroyAllWindows()


#4

# cap = cv2.VideoCapture(0)
# cap.set(10 , 1)

# blackimg = np.ones((5,5) , np.uint8)
# print(blackimg0)
# while True:
#     s , img = cap.read()
#     imgcanny = cv2.Canny(img , 0 , 300)
#     imgd = cv2.dilate( imgcanny , blackimg , iterations=1)
#     cv2.imshow("cannycam" , imgcanny)
#     cv2.imshow("imgdialation" , imgd)
#     cv2.imshow("cam" , img)
#     if cv2.waitKey(1) & 0xFF ==ord('k'):
#         break
#     if cv2.waitKey(1) & 0xFF ==ord(' '):
#         break


#5


# img = cv2.imread("i.jpg")
# print(img.shape)
# imgresized = cv2.resize(img , (200 , 200))
# imgcroped  = img[0:200 , 200:400]
# print(imgresized.shape)
# print(img)
# cv2.imshow("resimg" , imgresized)
# cv2.imshow("cropedimg" , imgcroped)
# cv2.imshow("img" , img)
# cv2.waitKey(0)


#6


# img = np.ones((500,500,3),np.uint8)
# img[200:300 , 300:400] = 0,0,255
# cv2.line(img , (20,20) , (300 , 150) ,(255 , 0 , 0) , 9 )
# cv2.rectangle(img , (50 ,50) , (230 , 300) , (255 , 255 , 255) , cv2.FILLED )
# cv2.circle(img , (400 ,100) , 70 , (205 , 25 , 25) , cv2.FILLED )
# cv2.putText(img , "hello i am mehdi" , (100 , 450) , cv2.FONT_HERSHEY_DUPLEX, 1 , (0 , 255 , 70) , 1)
# cv2.imshow("img" , img)
# cv2.waitKey(0)


#7


# wth = 255
# hth = 320
# img = cv2.imread("v.jpg")
# points1= np.float32([[452 , 61] , [621, 54] , [500 , 334] ,[668, 307]])
# points2 = np.float32([[0, 0] , [wth , 0] , [0 , hth] ,[wth, hth]])
# matrix =  cv2.getPerspectiveTransform(points1, points2)
# imgout = cv2.warpPerspective(img , matrix , (wth , hth))
# cv2.imshow("out" , img)
# cv2.imshow("outim" , imgout)
# cv2.waitKey(0)


#8


# img = cv2.imread('i.jpg')
# img = cv2.resize(img , (300 , 200))
# imggray = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
# imgh = np.hstack((img , img))
# imgv = np.vstack((img , imggray))
# cv2.imshow("img" , img)
# cv2.imshow("imgh" , imgh)
# cv2.imshow("imgv" , imgv)
# cv2.imshow("imgg" , imggray)
# cv2.waitKey(0)


#9


# def emp(a):
#     pass
# cv2.namedWindow("bar")
# cv2.resizeWindow("bar" , 640 , 240)
# cv2.createTrackbar("hue min" , "bar" , 0 , 179 , emp)
# cv2.createTrackbar("hue max" , "bar" , 179 , 179 , emp)
# cv2.createTrackbar("sat min" , "bar" , 0 , 255 , emp)
# cv2.createTrackbar("sat max" , "bar" , 255 , 255 , emp)
# cv2.createTrackbar("val min" , "bar" , 0 , 255 , emp)
# cv2.createTrackbar("val max" , "bar" , 255 , 255 , emp)
# while True:
#     img = cv2.imread("benz.jpg")
#     img = cv2.resize(img , (300 , 200))
#     h_min = cv2.getTrackbarPos("hue min" , "bar")
#     h_max = cv2.getTrackbarPos("hue max" , "bar")
#     s_min = cv2.getTrackbarPos("sat min" , "bar")
#     s_max = cv2.getTrackbarPos("sat max" , "bar")
#     v_min = cv2.getTrackbarPos("val min" , "bar")
#     v_max = cv2.getTrackbarPos("val max" , "bar")
#     print(h_min , h_max , s_min , s_max , v_min , v_max)
#     hsvimg = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
#     lower  = np.array([h_min , s_min , v_min])
#     upper  = np.array([h_max , s_max , v_max])
#     mask = cv2.inRange(hsvimg , lower , upper)
#     imgresult = cv2.bitwise_and(img , img , mask=mask)
#     cv2.imshow("img" , img)
#     cv2.imshow("hsvimg" , hsvimg)
#     cv2.imshow("mask" , mask)
#     cv2.imshow("result" , imgresult)
#     if cv2.waitKey(1) & 0xFF ==ord(' '):
#          cv2.destroyAllWindows()
#          break


#10


# def getcontour(img):
#     contours , hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area>500:
#             cv2.drawContours(imgcontour , cnt , -1 , (255 , 0 , 0) , 1)
#             per = cv2.arcLength(cnt , True)
#             approx = cv2.approxPolyDP(cnt , 0.02*per , True)
#             obj = len(approx)
#             x , y , w , h = cv2.boundingRect(approx)
#             objectal = "none"
#             if obj ==3 :
#                 objectal = "tri"
#             elif obj ==4 :
#                 asp = w/float(h) 
#                 if asp > 0.95 and asp < 1.05:
#                     objectal = "square"
#                 else:
#                     objectal = "rect"
#             elif obj >4 :
#                 objectal = "circle"
#             elif obj ==3 :
#                 objectal = "tri"
#             cv2.rectangle(imgcontour , (x , y) , (x+w , y+h) , (0 , 150 , 255) , 1)
#             cv2.putText(imgcontour, objectal , ( x + (w//2) -10 , y +(h//2) -10) , cv2.FONT_HERSHEY_COMPLEX , 0.5, (0 , 0 , 0) , 1)
#             app = [x + (w//2) -10 , y +(h//2) -10 , objectal]
#             try:
#                 shape.append(app)
#             except:
#                 pass

# def liner(img , shap):
#     n = len(shap)
#     e = n/2
#     i = 1
#     w = []
#     sq = []
#     while i <= n:
#         w.append(shap[i-1][2])
#         i+=1
#     print(w)
#     s = 1
#     while s <= e:
#         try:
#             sq.append([w.index(w[s-1]) , w.index(w[s-1] , 4)])
#         except:
#             pass
#         print(sq)
#         s +=1
#     for ss in sq:
#         cv2.line(img , (shap[ss[0]][0],shap[ss[0]][1]) , (shap[ss[1]][0],shap[ss[1]][1]) ,(255 , 0 , 0) , 2)

# shape = []
# img = cv2.imread("shape.png")
# imgo = cv2.resize(img , (200 , 400))
# imgcontour = img.copy()
# imggray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(
# imggray , (7,7) , 1)
# cannyimg = cv2.Canny(imgblur, 50 , 50 )
# getcontour(cannyimg)
# print(shape)
# liner(imgcontour , shape)
# imgh = np.hstack((imggray , imgblur))
# cv2.imshow("canny image" , cannyimg)
# cv2.imshow("images"  , imgh)
# cv2.imshow("image"  , imgcontour)
# cv2.imshow("iage"  , img)
# cv2.waitKey(0)


#11


# mypointtt = []
# def drawpoint(mypoint):
#     for poi in mypoint:
#         cv2.circle(imagee , (poi[0],poi[1]) , 10 , (255,0 , 0) , cv2.FILLED)
        
# def getcontour(img):
#     contours , hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area>500:
#             cv2.drawContours(imag , cnt , -1 , (0,255,255) , 4)
#             per = cv2.arcLength(cnt , True)
#             approx = cv2.approxPolyDP(cnt , 0.02*per , True)
#             x , y , w , h = cv2.boundingRect(approx)    
#             cv2.circle(imagee , (x,y) , 10 , (255,0 , 0) , cv2.FILLED)
#             mypointtt.append([x,y])
# cap = cv2.VideoCapture(0)
# cap.set(10 , 1)

# while True:
#     suc , img = cap.read()
#     img = cv2.resize(img , (1600 , 800))
#     img = cv2.flip(img, 1)
#     imagee = img.copy()
#     hsvimg = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
#     lower  = np.array([101 , 116 , 78])
#     upper  = np.array([118 , 255 , 255])
#     mask = cv2.inRange(hsvimg , lower , upper)  
#     imgr = cv2.bitwise_and(img , img , mask=mask)
#     imag = img.copy()
#     getcontour(mask)
#     drawpoint(mypointtt)
#     # cv2.imshow("maskimage"  , mask)
#     # cv2.imshow("result"  , imgr)
#     # cv2.imshow("resulft"  , imag)
#     cv2.imshow("resul"  , imagee)
#     if cv2.waitKey(1) & 0xFF ==ord(' '):
#          cv2.destroyAllWindows()
#          break