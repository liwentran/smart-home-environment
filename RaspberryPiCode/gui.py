from tkinter import *
isTouched = 0

def on_click():
    print('Click')
    
class MyWindow:
    def __init__(self, win):
        self.lbl_touchsensor = Label(win, text="Touch Sensor: ", fg='white').grid(row=0, column=0)
        self.lbl_touchsensor_output = Label(win, text="{isTouched}", fg='white').grid(row=0, column=1)
        self.btn_reinit = Button(win, text='Re-init', padx=40, pady=20, command=on_click).grid(row=1, column=0)
        

window = Tk()
mywin = MyWindow(window)
window.title('Home Environment')
window.mainloop()
 
