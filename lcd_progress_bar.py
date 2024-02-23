import rpi_lcd as lcd
from time import sleep
from random import *


screen=lcd.LCD()
screen.text("Progress:", 1)

MAX_SCREEN_DIGITS=17





for i in range(0, MAX_SCREEN_DIGITS):
    remaining=MAX_SCREEN_DIGITS-i
    print("Progress: "+i*"#"+remaining*".", end="|\r")
    screen.text(i*"#"+remaining*".", 2)
    sleep(uniform(0.0625, 3))


print("\n")
screen.clear()




