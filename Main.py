
""" Interpolation Computational Mathematics Final Project """ 

import tkinter
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import tkinter.font as font


class Interpolation(Tk):
# the main frame 

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("Interpolation")
        self.switchFrame(mainMenu)
        self.geometry('800x600')
        self.config(bg = "black")

#switch in between the frames 

 #to initiate a new frame : 
 #class Introduction(Frame):

    #def __init__(self, master):
        #Frame.__init__(self, master)
        #self.config(bg = "black")

    def switchFrame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        

#main menu 
class mainMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        label = Label(self, text = "Computational Mathematics"\
                      , bg = "blue", fg = "white")
        label.pack()

        labelName = Label(self, text = "by Rohan, Raphael, and Ardelia")
        labelName.pack() 
       
        button = Button(self, text = "Introduction", width = 20, command = lambda: master.switchFrame(Introduction))
        button.pack(padx = 10, pady = 10)
        button2 = Button(self, text = "Langrange", width = 20, command = lambda: master.switchFrame(Langrange))
        button2.pack()
        button3 = Button(self, text = "Exit", width = 20, command = self.close)
        button3.pack(padx = 10, pady = 10)

    def close(self):
        self.destroy()
        exit()

class Introduction(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        #basic langrange 

        x =np.array([0, 20, 40, 60, 80, 100], float)
        y =np.array([26.0, 48.6, 61.6, 71.2, 74.8, 75.2], float) 
        
        xplt = np.linspace(x[0], x[-1])
        yplt = np.array([], float)
        
        for xp in xplt:
            yp = 0
            for xi,yi in zip(x,y): #iterator of array x and y 
                yp += yi * np.prod(( xp - x[x != xi]) / (xi - x[x != xi]))
            yplt = np.append(yplt,yp)
            
            
        f = Figure(figsize=(5,5), dpi = 100)
        a = f.add_subplot(111)
        a.plot(x,y, 'ro', xplt, yplt, 'b-')
        
        canvas = FigureCanvasTkAgg(f, self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        buttonLang = Button(self, text = "MainMenu", width = 500, command = lambda: master.switchFrame(mainMenu))
        buttonLang.pack()


class Langrange(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

          

if __name__ == "__main__":
    app = Interpolation()
    app.mainloop()