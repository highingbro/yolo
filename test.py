import cv2
import time
capture1 = cv2.VideoCapture(0)
#capture2= cv2.VideoCapture(6)
print("press space to take a picture,press q to quit")
count = 1
while(True):
    ret1, frame1 = capture1.read()
    #ret2, frame2 = capture2.read()
    # gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame1', frame1)
    #cv2.imshow('frame2', frame2)q
    if(cv2.waitKey(1)==ord(' ')):
        filename=f'photo_{count}.jpg'
        count+=1
        # cv2.imwrite(filename, gray)
        cv2.imwrite(filename, frame1)
    elif(cv2.waitKey(1)==ord('q')):
        break 梦游