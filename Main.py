
""" Interpolation Computational Mathematics Final Project """ 

import tkinter
from tkinter import *
from tkinter import messagebox as mb
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import tkinter.font as font
import functions



class Interpolation(Tk):
# the main frame 

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("Interpolation")
        self.switchFrame(mainMenu)
        self.config(bg = "white")

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
        self.config(bg = "white")

        label = Label(self, text = "Computational Mathematics"\
                      , bg = "blue", fg = "white")

        label.config(font=("Courier", 21))
        label.pack(padx = 15, pady = 15)

        labelName = Label(self, text = "by Rohan, Raphael, and Ardelia")
        labelName.config(font=("Courier", 10))
        labelName.pack() 
       
        button = Button(self, text = "Introduction", bg = "black", fg = "white", width = 30, command = lambda: master.switchFrame(Introduction))
        button.pack(padx = 10, pady = 5)
        button.config(font=("Courier", 12))

        button2 = Button(self, text = "Langrange",bg = "black", fg = "white",  width = 30, command = lambda: master.switchFrame(Langrange))
        button2.pack(padx = 10, pady = 5)
        button2.config(font=("Courier", 12))

        button3 = Button(self, text = "Newton",bg = "black", fg = "white",  width = 30, command = lambda: master.switchFrame(Newton))
        button3.pack(padx = 10, pady = 5)
        button3.config(font=("Courier", 12))

    def close(self):
        self.destroy()
        exit()

#main menu 
class mainMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "white")

        label = Label(self, text = "Computational Mathematics"\
                      , bg = "blue", fg = "white")

        label.config(font=("Courier", 21))
        label.pack(padx = 15, pady = 15)

        labelName = Label(self, text = "by Rohan, Raphael, and Ardelia")
        labelName.config(font=("Courier", 10))
        labelName.pack() 
       
        button = Button(self, text = "Introduction", bg = "black", fg = "white", width = 30, command = lambda: master.switchFrame(Introduction))
        button.pack(padx = 10, pady = 5)
        button.config(font=("Courier", 12))

        button2 = Button(self, text = "Langrange",bg = "black", fg = "white",  width = 30, command = lambda: master.switchFrame(Langrange))
        button2.pack(padx = 10, pady = 5)
        button2.config(font=("Courier", 12))

        button3 = Button(self, text = "Newton",bg = "black", fg = "white",  width = 30, command = lambda: master.switchFrame(Newton))
        button3.pack(padx = 10, pady = 5)
        button3.config(font=("Courier", 12))

    def close(self):
        self.destroy()
        exit()

class Introduction(Frame):
    # linear Interpolation

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        mainframe = Frame(self, bd=50)
        mainframe.pack(fill=BOTH, expand=YES)

        frData = Frame(mainframe, bd=50)
        frData.pack(fill=BOTH, expand=YES)

        Label(frData, text='Linear Interpolation').grid(row=0, column=0, sticky=W)
        self.name = Label(frData)

        Label(frData, text='x0:').grid(row=1, column=0, sticky=W)
        self.entryx0 = Entry(frData)
        self.entryx0.grid(row=1, column=1)

        Label(frData, text='x1:').grid(row=2, column=0, sticky=W)
        self.entryx1 = Entry(frData)
        self.entryx1.grid(row=2, column=1)

        Label(frData, text='y0:').grid(row=3, column=0, sticky=W)
        self.entryy0 = Entry(frData)
        self.entryy0.grid(row=3, column=1)
        
        Label(frData, text='y1:').grid(row=4, column=0, sticky=W)
        self.entryy1 = Entry(frData)
        self.entryy1.grid(row=4, column=1)

        Label(frData, text='xp:').grid(row=5, column=0, sticky=W)
        self.entryxp = Entry(frData)
        self.entryxp.grid(row=5, column=1)

        frTombol = Frame(mainframe, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)

        frTombol = Frame(mainframe, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)

        self.btnCalculate = Button(frTombol, text='Calculate', command = self.calculate_linear)
        self.btnCalculate.pack(side=LEFT, fill=BOTH, expand=YES)



    def calculate_linear(self):
        try:
            x0Value = self.entryx0.get()
            x0 = int(x0Value)
        except ValueError:
            mb.showwarning('Wrong input', 'value is not valid')
            self.entryx0.focus_set()
            return
            
        try:
            x1Value = self.entryx1.get()
            x1 = int(x1Value)
        except ValueError:
            mb.showwarning('Wrong input', 'value is not valid')
            self.entryx1.focus_set()
            return
        
        try:
            y0Value = self.entryy0.get()
            y0 = int(y0Value)
        except ValueError:
            mb.showwarning('Wrong input', 'Age is not valid')
            self.entryy0.focus_set()
            return

        try:
            y1Value= self.entryy1.get()
            y1= int(y1Value)
        except ValueError:
            mb.showwarning('Wrong input', 'Age is not valid')
            self.entryy1.focus_set()
            return

        try:
            xpValue = self.entryxp.get()
            xp = int(xpValue)
        except ValueError:
            mb.showwarning('Wrong input', 'Age is not valid')
            self.entryxp.focus_set()
            return
        
        yp = y0 + (y1-y0)/(x1-x0) * (xp - x0)
        Answer = yp
        mb.showinfo("Results: ",Answer, parent = self)

class results(Frame):
     def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "white")




        # x =np.array([0, 20, 40, 60, 80, 100], float)
        # y =np.array([26.0, 48.6, 61.6, 71.2, 74.8, 75.2], float) 

        # xplt = np.linspace(x[0], x[-1])
        # yplt = np.array([], float)
        
        # for xp in xplt:
        #     yp = 0
        #     for xi,yi in zip(x,y): #iterator of array x and y 
        #         yp += yi * np.prod(( xp - x[x != xi]) / (xi - x[x != xi]))
        #     yplt = np.append(yplt,yp)
             
            
        # f = Figure(figsize=(5,5), dpi = 100)
        # a = f.add_subplot(111)
        # a.plot(x,y, 'ro', xplt, yplt, 'b-')

        # canvas = FigureCanvasTkAgg(f, self)  # A tk.DrawingArea.
        # canvas.draw()
        # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        # toolbar = NavigationToolbar2Tk(canvas, self)
        
        # toolbar.update()
        # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        #  #show the y value when x is known
        # labelLang = Label(self, text =x)
        # labelLang.pack() 

        # labelLang2 = Label(self, text =y)
        # labelLang2.pack() 


        buttonLang = Button(self, text = "MainMenu", width = 500, command = lambda: master.switchFrame(mainMenu))
        buttonLang.pack()


        #print(' for x = %.2f, y = %f' % (xp1,yp1))


class Langrange(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")
        
        #basic langrange 




class Newton(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")




x1 = [0,20,40,60,80,100]
y1 = [26,48.6, 64.3, 71.2, 74.8, 80.9]
         



if __name__ == "__main__":
    app = Interpolation()
    app.mainloop()


    #to change font size - label.config(font=("Helvetica", 44))
