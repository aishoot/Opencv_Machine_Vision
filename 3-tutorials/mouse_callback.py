# Capture video from Camera or video files and save video
import numpy as np
import cv2

# Test events in OpenCV
events = [i for i in dir(cv2) if "EVENT" in i]
print(events)

# Parameters
drawing = False
mode = True
ix, iy = -1, -1

# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDBLCLK: # 左键双击
        #cv2.circle(img, (x,y), 100, (255,0,0), -1)
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:  # 滑动
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
            else:
                cv2.circle(img, (x,y), 5, (0,0,255), -1)

    elif event == cv2.EVENT_LBUTTONUP:  # 左键放开
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
        else:
            cv2.circle(img, (x,y), 5, (0,0,255), -1)


# Create a black image, a window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_circle)

while(1):
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()