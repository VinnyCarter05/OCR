import pytesseract
from PIL import Image
import cv2
from QOveride import Worker
import time
import numpy as np

path = "page_3.jpg"

def tesspage (path):
    img = cv2.imread(path)

    # ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

    # pytesseract image to string to get results
    text = str(pytesseract.image_to_string(img, config='--psm 6'))
    print(text)

    # print(pytesseract.image_to_string(Image.open(path)))

    print(pytesseract.image_to_data(img, config='--psm 6'))

def tesseractPage (path):
    img = cv2.imread(path)

    text = str(pytesseract.image_to_string(img, config='--psm 6'))
    print(text)
    worker.signal.emit(100000)

    kernel = np.ones((1,1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.GaussianBlur(img, (5,5), 0)
    img = cv2.medianBlur(img,5)

    text = str(pytesseract.image_to_string(img, config='--psm 6'))
    print(text)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
    img = adaptive_threshold

    text = str(pytesseract.image_to_string(img, config='--psm 6'))
    print(text)

def receive(sig):
    print (sig)



worker = Worker(tesseractPage, path)
worker.signal.connect(receive)
print (type (worker))
worker.start()
i = 1
while not worker.isFinished():
    print (i)
    time.sleep(1)
    if i%5 == 0:
        worker.signal.emit(100*i)
    i+=1
