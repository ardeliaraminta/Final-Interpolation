""" Interpolation Computational Mathematics Final Project """ 

import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import tkinter.font as font

Interpolation = Tk()
frame = Frame(Interpolation)
frame.pack()

Interpolation.geometry('1000x600')
Interpolation.config(bg = "Powder Blue")
Interpolation.title( "Computational Mathematics: Interpolation")

switchFrame = ttk.Notebook(Interpolation)
switchFrame.pack() 

Lagrange= Frame(switchFrame, width = 1000, height = 600, bg = "Powder blue")
Lagrange.pack(fill = "both", expand = 1)

Newton = Frame(switchFrame, width = 1000, height = 600, bg = "Powder blue")
Newton.pack(fill = "both", expand = 1)

linear = Frame(switchFrame, width = 1000, height = 600, bg = "Powder blue")
linear.pack(fill = "both", expand = 1)

switchFrame.add(Lagrange, text = "Langrange")
switchFrame.add(Newton, text = "Newton")
switchFrame.add(linear, text =  " Linear ")


# Langrange 

# labelLang = Label(Lagrange, text ='Lagrange', font = ("Helvetica", 15))
# labelLang.place(x = 400, y = 5)

xValue = []
yValue = []
xp = 0


def setx():
    try:
        XValues = entryXValues.get().split(",")
        xValue = [float(x) for x in XValues]
        # to check if the value return
        mb.showinfo("X Values:", xValue)
    except ValueError:
        mb.showwarning('Wrong input', 'value is not valid')
        entryXValues.focus_set()
        return

def sety():
    try:
        YValues = entryYValues.get().split(",")
        yValue = [float(x) for x in YValues]
        mb.showinfo("Y Values:", yValue.length)
    except ValueError:
        mb.showwarning('Wrong input', 'value is not valid')
        entryYValues.focus_set()

def xp():  
    try:
        xpValue = entryxp.get()
        xp = float(xpValue)
    except ValueError:
        mb.showwarning('Wrong input', 'Value entered is not valid')
        entryxp.focus_set()
        return


def lagrange(size,xp,xarray,yarray):

    global xValue
    global yValue

    yp = 0

    # Implementing Lagrange Interpolation
    for i in range(size):
        p = 1
        
        for j in range(size):
            if i != j:
                p = p * (xp - xValue[j])/(xValue[i] - xValue[j])
        
        yp = yp + p * yValue[i]

        Result = yp 
        mb.showinfo("yp: ",Result,Lagrange)
        

labelX= Label(Lagrange, text = "X Values Entries: ", bg = "black", fg = "white")
labelX.config(font=("Courier", 11))
labelX.pack()

entryXValues = Entry(Lagrange, width = 30, bg = "white")
entryXValues.pack()

labelY= Label(Lagrange, text = "Y Values Entries: ", bg = "black", fg = "white")
labelY.config(font=("Courier", 11))
labelY.pack()

entryYValues = Entry(Lagrange, width = 30, bg = "white")
entryYValues.pack()

labelxp= Label(Lagrange, text = "Value of xp: ", bg = "black", fg = "white")
labelxp.config(font=("Courier", 10))
labelxp.pack()

entryxp = Entry(Lagrange, width = 30, bg = "white")
entryxp.pack()

buttonResult = Button(Lagrange, text = " Result ", bg = "DeepSkyBlue4", fg = "white", width = 25, command = lambda:lagrange(len(xValue), xp, xValue, yValue))
buttonResult.pack(padx = 10, pady = 5)
buttonResult.config(font=("Courier", 11))


#Linear              

labelx0= Label(linear, text = "Value of x0: ", bg = "DodgerBlue4", fg = "white")
labelx0.config(font=("Courier", 10))
labelx0.pack()

entryx0 = Entry(linear, width = 30, bg = "white")
entryx0.pack()

labelx1= Label(linear, text = "Value of x1: ", bg = "DodgerBlue4", fg = "white")
labelx1.config(font=("Courier", 10))
labelx1.pack()

entryx1 = Entry(linear, width = 30, bg = "white")
entryx1.pack()

labely0= Label(linear, text = "Value of y0: ", bg = "DodgerBlue4", fg = "white")
labely0.config(font=("Courier", 10))
labely0.pack()

entryy0 = Entry(linear, width = 30, bg = "white")
entryy0.pack()

labely1= Label(linear, text = "Value of y1: ", bg = "DodgerBlue4", fg = "white")
labely1.config(font=("Courier", 10))
labely1.pack()

entryy1 = Entry(linear, width = 30, bg = "white")
entryy1.pack()

labelxp= Label(linear, text = "Value of xp: ", bg = "DodgerBlue4", fg = "white")
labelxp.config(font=("Courier", 10))
labelxp.pack()



entryxp = Entry(linear, width = 30, bg = "white")
entryxp.pack()




def linear_interpolation():
    try:
        x0Value = entryx0.get()
        x0 = float(x0Value)
    except ValueError:
        mb.showwarning('Wrong input', 'value is not valid')
        entryx0.focus_set()
        return
        
    try:
        x1Value = entryx1.get()
        x1 = float(x1Value)
    except ValueError:
        mb.showwarning('Wrong input', 'Value entered is not valid')
        entryx1.focus_set()
        return
    
    if x0 > x1:
        mb.showwarning("Error", " x0 should be less than x1")
        return
    
    try:
        y0Value = entryy0.get()
        y0 = float(y0Value)
    except ValueError:
        mb.showwarning('Wrong input', 'Value entered is not valid')
        entryy0.focus_set()
        return

    try:
        y1Value = entryy1.get()
        y1= float(y1Value)
    except ValueError:
        mb.showwarning('Wrong input', 'Value entered is not valid')
        entryy1.focus_set()
        return

    try:
        xpValue = entryxp.get()
        xp = float(xpValue)

        if xp < x0 or xp > x1:
            mb.showwarning(" ERROR WARNING!!", "should be in between x0 and x1" )
            return

    except ValueError:
        mb.showwarning('Wrong input', 'Value entered is not valid')
        entryxp.focus_set()
        return
    
    yp = y0 + (y1-y0)/(x1-x0) * (xp - x0)
    Answer = yp
    mb.showinfo("yp and graph ",Answer, parent = linear)

    f = Figure(figsize=(5,5), dpi = 100)
    a = f.add_subplot(111)
    a.plot(([x0, xp ,x1 ]),([y0, yp, y1]), 'ro',([x0, xp ,x1 ]),([y0, yp, y1]), 'b-')

    canvas = FigureCanvasTkAgg(f, linear)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, linear)

    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

button = Button(linear, text = "Yp Value and Graph", bg = "black", fg = "white", width = 30, command = linear_interpolation)
button.pack(padx = 10, pady = 5)
button.config(font=("Courier", 12))

mainloop()