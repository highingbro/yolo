import cv2
capture = cv2.VideoCapture(6)


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
outfile = cv2.VideoWriter('output.mp4', fourcc, 25., (640, 480))

while(capture.isOpened()):
    ret, frame = capture.read()

    if ret:
        outfile.write(frame)  
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
