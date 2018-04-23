# Capture video from Camera or video files and save video
import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # Read from camera
#cap = cv2.VideoCapture("fish.mp4")  # Read from video file

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()  # Capture frame by frame
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("frame", gray)
    if ret == True:
        frame = cv2.flip(frame, 0)
        out.write(frame)  # write the flipped frame
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the capture
cap.release()
out.release()
cv2.destroyAllWindows()