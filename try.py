import pytesseract
from PIL import Image
import cv2

path = "page_3.jpg"

img = cv2.imread(path)

# ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

# pytesseract image to string to get results
text = str(pytesseract.image_to_string(img, config='--psm 6'))
print(text)

# print(pytesseract.image_to_string(Image.open(path)))

print(pytesseract.image_to_data(img, config='--psm 6'))