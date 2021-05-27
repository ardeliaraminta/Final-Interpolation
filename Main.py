
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
       
        button0 = Button(self, text = "Linear Interpolation yp = 0", bg = "black", fg = "white", width = 30, command = lambda: master.switchFrame(LinearInterpolation))
        button0.pack(padx = 10, pady = 5)
        button0.config(font=("Courier", 12))

        button = Button(self, text = "Linear Interpolation xp = 0", bg = "black", fg = "white", width = 30, command = lambda: master.switchFrame(LinearInterpolation2))
        button.pack(padx = 10, pady = 5)
        button.config(font=("Courier", 12))


        button2 = Button(self, text = "Basic Langrange",bg = "black", fg = "white",  width = 30, command = lambda: master.switchFrame(Langrange))
        button2.pack(padx = 10, pady = 5)
        button2.config(font=("Courier", 12))

        button3 = Button(self, text = "Newton",bg = "black", fg = "white",  width = 30, command = lambda: master.switchFrame(Newton))
        button3.pack(padx = 10, pady = 5)
        button3.config(font=("Courier", 12))

    def close(self):
        self.destroy()
        exit()

class LinearInterpolation(Frame):
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

        self.btnCalculate = Button(frTombol, text='Calculate', command = self.linear_interpolation)
        self.btnCalculate.pack(side=LEFT, fill=BOTH, expand=YES)

    #linear interpolation
    def linear_interpolation(self):
        y = 0
    
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
            mb.showwarning('Wrong input', 'Value entered is not valid')
            self.entryx1.focus_set()
            return
        
        try:
            y0Value = self.entryy0.get()
            y0 = int(y0Value)
        except ValueError:
            mb.showwarning('Wrong input', 'Value entered is not valid')
            self.entryy0.focus_set()
            return

        try:
            y1Value= self.entryy1.get()
            y1= int(y1Value)
        except ValueError:
            mb.showwarning('Wrong input', 'Value entered is not valid')
            self.entryy1.focus_set()
            return

        try:
            xpValue = self.entryxp.get()
            xp = int(xpValue)
        except ValueError:
            mb.showwarning('Wrong input', 'Value entered is not valid')
            self.entryxp.focus_set()
            return

        yp = y0 + (y1-y0)/(x1-x0) * (xp - x0)
        Answer = yp
        mb.showinfo("Yp: ",Answer, parent = self)


class LinearInterpolation2(Frame):
    # linear Interpolation

    def __init__(self, master):

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

        Label(frData, text='yp:').grid(row=5, column=0, sticky=W)
        self.entryyp = Entry(frData)
        self.entryyp.grid(row=5, column=1)

        frTombol = Frame(mainframe, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)

        frTombol = Frame(mainframe, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)

        self.btnCalculate = Button(frTombol, text='Calculate', command = self.linear_interpolation2)
        self.btnCalculate.pack(side=LEFT, fill=BOTH, expand=YES)

    #linear interpolation
    def linear_interpolation2(self):
        try:
            x0Value = self.entryx0.get()
            x0 = float(x0Value)
        except ValueError:
            mb.showwarning('Wrong input', 'value is not valid')
            self.entryx0.focus_set()
            return
            
        try:
            x1Value = self.entryx1.get()
            x1 = float(x1Value)
        except ValueError:
            mb.showwarning('Wrong input', 'Value entered is not valid')
            self.entryx1.focus_set()
            return
        
        try:
            y0Value = self.entryy0.get()
            y0 = float(y0Value)
        except ValueError:
            mb.showwarning('Wrong input', 'Value entered is not valid')
            self.entryy0.focus_set()
            return

        try:
            y1Value= self.entryy1.get()
            y1= float(y1Value)
        except ValueError:
            mb.showwarning('Wrong input', 'Value entered is not valid')
            self.entryy1.focus_set()
            return

        try:
            ypValue = self.entryyp.get()
            yp = float(ypValue)
        except ValueError:
            mb.showwarning('Wrong input', 'Value entered is not valid')
            self.entryxp.focus_set()
            return
    
        xp = 0 
        xp=(yp-y0)/((y1-y0)/(x1-x0))+x0
        Answer2 = xp
        mb.showinfo("Xp: ",Answer2, parent = self)


class results(Frame):
     def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "white")


class Langrange(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        labelX= Label(self, text = "X Values Entries: ", bg = "black", fg = "white")
        labelX.config(font=("Courier", 11))
        labelX.pack()

        entryXValues = Entry(self, width = 30, bg = "white")
        entryXValues.pack()

        labelY= Label(self, text = "Y Values Entries: ", bg = "black", fg = "white")
        labelY.config(font=("Courier", 11))
        labelY.pack()

        entryYValues = Entry(self, width = 30, bg = "white")
        entryYValues.pack()

        
        def setX():
            """ it will take x values and y values 
             user has to enter values seperated by comma to create an array"""
            
            try:
                XValues = entryXValues.get().split(",")
                xValue = [float(x) for x in XValues]
                # to check if the value return
                mb.showinfo("X Values:", xValue)
            except ValueError:
                mb.showwarning('Wrong input', 'value is not valid')
                entryXValues.focus_set()
                return
           
        def setY():
            try:
                YValues = entryYValues.get().split(",")
                yValue = [float(x) for x in YValues]
                mb.showinfo("Y Values:", yValue)
            except ValueError:
                mb.showwarning('Wrong input', 'value is not valid')
                entryYValues.focus_set()
                return

        ButtonX = Button(self, text = "Get X Values",  command = setX)
        ButtonX.pack() 

        ButtonY = Button(self, text = "Get Y Values",  command = setY)
        ButtonY.pack() 

       







        

                




class Newton(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")



if __name__ == "__main__":
    app = Interpolation()
    app.mainloop()

#FRONT END NOTES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

#to change font size - label.config(font=("Helvetica", 44))
# entry = "0,8,0,1,0,0"

# nameSplit = entry.split(",")
# numbers = [int(x) for x in nameSplit]

# print(nameSplit)
# print(numbers)
