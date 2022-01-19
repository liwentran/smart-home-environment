import tkinter as tk
import random
import sensors

def init():
    print("Initializing...")
    # init GPIO board
    print("Initialization complete")
    pass
def clean():
    print("Cleaning up...")
    # turn off things
    print("Clean up complete")
    pass

class Window:

    def __init__(self, win):
        win.title('Home Environment')
        #win.geometry('600x400+50+50')
        self.touch_state = 0    
        init()
        self.win = win
        self.lbl_touchsensor = tk.Label(win, text="Touch Sensor: ").grid(row=0, column=0)
        self.lbl_touchsensor_output = tk.Label(win, text=mock_sensor.get_state())
        self.lbl_touchsensor_output.grid(row=0, column=1)
        self.btn_reinit = tk.Button(win, text='Init', padx=40, pady=20, command=init).grid(row=1, column=0)
        self.btn_quit = tk.Button(win, text='Quit', padx=40, pady=20, command=self.cleanup).grid(row=1, column=1)
        pass

    def cleanup(self):
        clean()
        self.win.destroy()
        pass

    def update(self):
        self.lbl_touchsensor_output.config(text=mock_sensor.get_state())
        self.win.after(1000, self.update)


mock_sensor = sensors.MockSensor()
root = tk.Tk()
mywin = Window(root)
mywin.update()
root.mainloop()
