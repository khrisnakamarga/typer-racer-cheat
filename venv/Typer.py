from pynput.keyboard import Key, Controller
import time

f = open("type.txt", "r")

time.sleep(1)
keyboard = Controller()
keyboard.type(f.readlines())

