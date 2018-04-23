import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img/build.png", cv2.IMREAD_COLOR)
cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 窗口可调整大小
cv2.imshow("image", img) # 窗口名必须与上面一致

k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord("s"):  # wait for "s" to wave and exit
    cv2.imwrite("test.png", img)
    cv2.destroyAllWindows()

# Use matplotlib
plt.imshow(img, cmap = "gray", interpolation = "bicubic")
plt.xticks([]), plt.yticks([])  # hide tick value
plt.show()
