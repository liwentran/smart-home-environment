from tkinter import *
from threading import Thread
import RPi.GPIO as GPIO
from time import sleep
import os

# pin values
sensor = 26
light = 18


# LED light bulb
class LED:
    # LED init
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT, initial=0)
        pass

    # turn on LED
    def on(self):
        GPIO.output(self.pin, 1)
        pass

    # turn off LED
    def off(self):
        GPIO.output(self.pin, 0)
        pass

    # LED blinks once
    def blink_once(self):
        self.on()
        time.sleep(0.5)
        self.off()
        pass

# Kookye touch sensor
class TouchSensor:
    # tracks the state of the touch sensor
    touch_state = 0

    # touch sensor init
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        touch_state = self.get_state()
        pass

    # returns 1 if touched and 0 if not touched
    def get_state(self):
        touch_state = GPIO.input(self.pin)
        return touch_state

    # returns the state of touch sensor
    def __str__(self):
        s = "Touch Sensor State: "
        if (self.get_state() == 1):
            s += "Touched"
        else:
            s+= "Untouched"
        return s
        
# GPIO port init
def init():
    GPIO.setmode(GPIO.BCM)
    pass

# clean up
def cleanup():
    print("\nCleaning up...")
    GPIO.cleanup()
    print("Quit...")
    #window.destroy()
    pass

# main loop
def main():
    # init variables
    init()
    ts = TouchSensor(sensor)
    green_led = LED(light)
    
    while True:
        if (ts.get_state() == 1):
            green_led.on()
            pass
        else:
            green_led.off()
            pass
        print(ts)
        time.sleep(0.5)
    pass

def task():
    print('starting task...')
    sleep(1)
    print('done')
    
# create threads
t1 = Thread(target=task)
t2 = Thread(target=task)
t1.start()
t2.start()
t1.join()
t2.join()
print('tasks complete')

if __name__ == '__main__':
    try:
#        main()
        pass
    except KeyboardInterrupt:
        pass

cleanup()

"""
def thread_target():
    global stop_thread
    ts = TouchSensor(sensor)
    while True:
        if stop_thread:
            break
        print(ts.str())
        time.sleep(2)
        
class MyWindow:
    def __init__(self, win):
        init()
        self.lbl_touchsensor = Label(win, text="Touch Sensor: ", fg='white').grid(row=0, column=0)
        self.lbl_touchsensor_output = Label(win, text=touch_state, fg='white').grid(row=0, column=1)
        self.btn_reinit = Button(win, text='Init', padx=40, pady=20, command=init).grid(row=1, column=0)
        self.btn_quit = Button(win, text='Quit', padx=40, pady=20, command=cleanup).grid(row=1, column=1)
        

window = Tk()
mywin = MyWindow(window)
window.title('Home Environment')
t1 = threading.Thread(target=thread_target).start()
window.mainloop()
"""
