import pytesseract
import cv2
import re
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

# img = cv2.resize(img, (600, 360))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
meter1 = float(re.findall(r'^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$', pytesseract.image_to_string(img1))[0][0])
meter2 = float(re.findall(r'^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$', pytesseract.image_to_string(img2))[0][0])
print(meter1)
print(meter2)
print("Difference")
print(round(meter2-meter1, 1))
# cv2.imshow('Result', img)
# cv2.waitKey(0)