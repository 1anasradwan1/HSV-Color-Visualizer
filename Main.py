import cv2
import numpy as np
def nothing(x):
    pass

cv2.namedWindow("frame")
cv2.createTrackbar("H", "frame", 0, 179, nothing)
cv2.createTrackbar("S", "frame", 225, 225, nothing)
cv2.createTrackbar("V", "frame",225, 225, nothing)
img_hsv=np.zeros((300, 512, 3), np.uint8)
while True:
    h=cv2.getTrackbarPos("H", "frame")
    s=cv2.getTrackbarPos("S", "frame")
    v=cv2.getTrackbarPos("V", "frame")
    img_hsv[:] = [h, s, v]
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow("frame", img_bgr)
    key = cv2.waitKey(1) 
    if key == 27:  # ESC key
        break
cv2.destroyAllWindows()