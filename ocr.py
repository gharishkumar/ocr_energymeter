import pytesseract
import cv2

img = cv2.imread('1.jpg')
# img = cv2.resize(img, (600, 360))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print(pytesseract.image_to_string(img))
cv2.imshow('Result', img)
cv2.waitKey(0)