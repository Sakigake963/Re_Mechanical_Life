import cv2
import colorsys

def hsv():
    img = cv2.imread("/home/pi/mll/Re_Mechanical_Life/foodrecog/foods/camera_1.jpg")
    bgr = img[239,319]
    num = bgr[0:3]
    hsv = colorsys.rgb_to_hsv(bgr[2],bgr[1],bgr[0])
    print(str(hsv))
    return hsv[2]

value = hsv()
print(value)
