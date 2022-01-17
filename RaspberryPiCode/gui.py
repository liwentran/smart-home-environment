from tkinter import *

import RPi.GPIO as GPIO
import time
import os
import queue

the_queue = queue.Queue()

# pin values
sensor = 26
light = 18

# tracks state of touch sensor
touch_state = 0;

# GPIO port init
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(light, GPIO.OUT, initial=0)
    GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    pass

# read touch sensor
def read_touchsensor():
    touch_state = GPIO.input(sensor)
    if(touch_state == True):
        print("Touch sensor: touched")
        light_on()
    else:
        print("Touch sensor: not touched")
        light_off()
    pass

# turn off LED
def light_on():
    GPIO.output(light,1)
    pass

# turn on LED
def light_off():
    GPIO.output(light,0)
    pass

# flash on and off LED
def light_flash():
    light_on()
    time.sleep(0.5)
    light_off()
    time.sleep(0.5)
    pass

# clean up
def cleanup():
    print("\nCleaning up...")
    light_off()
    GPIO.cleanup()
    print("Quit...")

def thread_target():
    while True:
        read_touchsensor()
        time.sleep(0.5)
        
    
class MyWindow:
    def __init__(self, win):
        init()
        self.lbl_touchsensor = Label(win, text="Touch Sensor: ", fg='white').grid(row=0, column=0)
        self.lbl_touchsensor_output = Label(win, text="${touch_state}", fg='white').grid(row=0, column=1)
        self.btn_reinit = Button(win, text='Init', padx=40, pady=20, command=init).grid(row=1, column=0)
        self.btn_quit = Button(win, text='Quit', padx=40, pady=20, command=cleanup).grid(row=1, column=1)
        

window = Tk()
mywin = MyWindow(window)
window.title('Home Environment')
threading.Thread(target=thread_target).start()
window.mainloop()

# we get here when the user closed the window
the_queue.put(none)
