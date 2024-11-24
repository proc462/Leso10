# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2

cap = cv2.VideoCapture("C:/Users/proho/Desktop/Jetlearn/OpenCV/Leso10/cars.mp4")

haar_file = "C:/Users/proho/Desktop/Jetlearn/OpenCV/Leso10/cars.xml"
car_cascade = cv2.CascadeClassifier(haar_file)

while True:
    (ret, img) = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,231,122),2)
    cv2.imshow('cars', img)
    if cv2.waitKey(33) == 27:
        break
cv2.destroyAllWindows()

#1. Decide what your going to use, whtere it is webcam or something else
#2. Get the haar file path and put it into your code
#3. Initialise the haar file with cascade classifier

#1. create an infinite loop (while True:)
#2. read the capture 
#3. convert it into grayscale
#4. Draw the rectangle 
