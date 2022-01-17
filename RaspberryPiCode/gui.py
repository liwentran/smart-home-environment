from tkinter import *
import multiprocessing
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
    # end thread
    proc_sensors.terminate()
    print("Quit...")
    # close window
    window.destroy()
    pass


def read_sensors(win):
    while True:
        # print out the value of the touch sensor every 0.5 seconds
        print(ts)
        sleep(0.5)
        win.update()

class MyWindow:
    def __init__(self, win):
        init()
        # holds ts value
        self.ts_value = StringVar()

        # widgets
        self.lbl_ts = Label(win, text="Touch Sensor: ")
        self.lbl_ts.grid(row=0, column=0)
        self.lbl_ts_value = Label(win, text=self.ts_value.get())
        self.lbl_ts_value.grid(row=0, column=1)
        self.btn_reinit = Button(win, text='Init', padx=40, pady=20, command=init).grid(row=1, column=0)
        self.btn_quit = Button(win, text='Quit', padx=40, pady=20, command=cleanup).grid(row=1, column=1)
        pass

    # attempts to update label value
    def update(self):
        state = str(ts.get_state())
        self.ts_value.set(state)


# init sensors and board
init()
ts = TouchSensor(sensor)
green_led = LED(light)

# create tkinter window
window = Tk()
mywin = MyWindow(window)
window.title('Home Environment')

# a thread to collect sensor data
proc_sensors = multiprocessing.Process(target=read_sensors, args=(mywin,))
proc_sensors.start()    

window.mainloop()
GPIO.cleanup()
