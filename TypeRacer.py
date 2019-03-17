from pynput.keyboard import Key, Controller
import time

import pytesseract
from PIL import Image
value = Image.open("Capture.png")

from PIL import Image

global keyboard
keyboard = Controller()

def main():
    image = Image.open("Capture.png", mode='r')
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    new_size = tuple(2*x for x in image.size)
    image = image.resize(new_size, Image.ANTIALIAS)
    text = pytesseract.image_to_string(image)
    text = text.replace("|", "I")
    text = text.replace("\n", " ")
    print(text)
    time.sleep(1)
    for letter in text:
        humanType(letter)

def humanType(letter):
    keyboard.press(letter)
    keyboard.release(letter)
    time.sleep(0.005)

if __name__ == "__main__":
    main()

'''
from pynput.keyboard import Key, Controller
import time

f = open("type.txt", "r")

time.sleep(2)
keyboard = Controller()
keyboard.type(f.readlines()[0])

'''