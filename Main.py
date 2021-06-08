""" Interpolation Computational Mathematics Final Project """ 

import tkinter
from tkinter import *
from tkinter import messagebox as mb
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import tkinter.font as font
import functions as fc



class Interpolation(Tk):
# the main frame 

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("Interpolation")
        self.switchFrame(mainMenu)
        self.config(bg ="powder blue")

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
        self.config(bg = "powder blue")

        label = Label(self, text = "Computational Mathematics"\
                      , bg = "DeepSkyBlue3", fg = "white")

        label.config(font=("Courier", 21))
        label.pack(padx = 15, pady = 15)

        labelName = Label(self, text = "by Rohan, Raphael, and Ardelia", fg = 'white', bg = "DodgerBlue4")
        labelName.config(font=("Courier", 10))
        labelName.pack() 
       
        button0 = Button(self, text = "Linear Interpolation", bg = "black", fg = "white", width = 30, command = lambda: master.switchFrame(LinearInterpolation))
        button0.pack(padx = 10, pady = 5)
        button0.config(font=("Courier", 12))

        # button = Button(self, text = "Linear Interpolation xp = 0", bg = "black", fg = "white", width = 30, command = lambda: master.switchFrame(LinearInterpolation))
        # button.pack(padx = 10, pady = 5)
        # button.config(font=("Courier", 12))


        button2 = Button(self, text = "Basic Langrange",bg = "black", fg = "white",  width = 30, command = lambda: master.switchFrame(Langrange))
        button2.pack(padx = 10, pady = 5)
        button2.config(font=("Courier", 12))

        button3 = Button(self, text = "Newton Forward",bg = "black", fg = "white",  width = 30, command = lambda: master.switchFrame(NewtonForward))
        button3.pack(padx = 10, pady = 5)
        button3.config(font=("Courier", 12))

        button4 = Button(self, text = "Newton Backward",bg = "black", fg = "white",  width = 30, command = lambda: master.switchFrame(NewtonBackward))
        button4.pack(padx = 10, pady = 5)
        button4.config(font=("Courier", 12))        

    def close(self):
        self.destroy()
        exit()

class LinearInterpolation(Frame):
    # linear Interpolation

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "DodgerBlue4")

        labelx0= Label(self, text = "Value of x0: ", bg = "DodgerBlue4", fg = "white")
        labelx0.config(font=("Courier", 10))
        labelx0.pack()

        entryx0 = Entry(self, width = 30, bg = "white")
        entryx0.pack()

        labelx1= Label(self, text = "Value of x1: ", bg = "DodgerBlue4", fg = "white")
        labelx1.config(font=("Courier", 10))
        labelx1.pack()

        entryx1 = Entry(self, width = 30, bg = "white")
        entryx1.pack()

        labely0= Label(self, text = "Value of y0: ", bg = "DodgerBlue4", fg = "white")
        labely0.config(font=("Courier", 10))
        labely0.pack()

        entryy0 = Entry(self, width = 30, bg = "white")
        entryy0.pack()
        
        labely1= Label(self, text = "Value of y1: ", bg = "DodgerBlue4", fg = "white")
        labely1.config(font=("Courier", 10))
        labely1.pack()

        entryy1 = Entry(self, width = 30, bg = "white")
        entryy1.pack()

        labelxp= Label(self, text = "Value of xp: ", bg = "DodgerBlue4", fg = "white")
        labelxp.config(font=("Courier", 10))
        labelxp.pack()

        entryxp = Entry(self, width = 30, bg = "white")
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
            mb.showinfo("yp and graph ",Answer, parent = self)

            f = Figure(figsize=(5,5), dpi = 100)
            a = f.add_subplot(111)
            a.plot(([x0, xp ,x1 ]),([y0, yp, y1]), 'ro',([x0, xp ,x1 ]),([y0, yp, y1]), 'b-')

            canvas = FigureCanvasTkAgg(f, self)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
            toolbar = NavigationToolbar2Tk(canvas, self)
        
            toolbar.update()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        button = Button(self, text = "Yp Value and Graph", bg = "white", fg = "black", width = 30, command = linear_interpolation)
        button.pack(padx = 10, pady = 5)
        button.config(font=("Courier", 12))

        buttonMain = Button(self, text = " Main Menu", bg = "white", fg = "black", width = 25, command = lambda: master.switchFrame(mainMenu))
        buttonMain.pack(padx = 10, pady = 5)
        buttonMain.config(font=("Courier", 12))


class results(Frame):
     def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "white")


class Langrange(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        
        def setx():
            global xValue
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

        def sety():
            global yValue
            global xp

            try:
                YValues = entryYValues.get().split(",")
                yValue = [float(x) for x in YValues]
                print(len(yValue))
                mb.showinfo("Y Values:",yValue)
            except ValueError:
                mb.showwarning('Wrong input', 'value is not valid')
                entryYValues.focus_set()
                
                
            try:
                xpValue = entryxp.get()
                xp = float(xpValue)
            except ValueError:
                mb.showwarning('Wrong input', 'Value entered is not valid')
                entryxp.focus_set()
                return


        def lagrange(size,xp,xarray,yarray):
             
            # Set interpolated value initially to zero
            yp = 0

            # Implementing Lagrange Interpolation
            for i in range(size):
                
                p = 1
                
                for j in range(size):
                    if i != j:
                        p = p * (xp - xarray[j])/(xarray[i] - xarray[j])
                
                yp = yp + p * yarray[i]
                
            Result = yp 
            mb.showinfo("yp: ",Result, parent = self)

            f = Figure(figsize=(5,5), dpi = 100)
            a = f.add_subplot(111)
            a.plot((xValue +[xp]),(yValue+[yp]), 'ro',(xValue +[xp]),(yValue+[yp]), 'b-')

            canvas = FigureCanvasTkAgg(f, self)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
            toolbar = NavigationToolbar2Tk(canvas, self)
        
            toolbar.update()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        

        def button_pressed():
            setx()
            sety()
            lagrange(len(xValue),xp, xValue, yValue)
        
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

        labelxp= Label(self, text = "Value of xp: ", bg = "black", fg = "white")
        labelxp.config(font=("Courier", 10))
        labelxp.pack()

        entryxp = Entry(self, width = 30, bg = "white")
        entryxp.pack()

        buttonResult = Button(self, text = " boho ", bg = "DeepSkyBlue4", fg = "white", width = 25, command = button_pressed)
        buttonResult.pack(padx = 10, pady = 5)
        buttonResult.config(font=("Courier", 11))

        
        buttonMain = Button(self, text = " Main Menu", bg = "white", fg = "black", width = 25, command = lambda: master.switchFrame(mainMenu))
        buttonMain.pack(padx = 10, pady = 5)
        buttonMain.config(font=("Courier", 12))
         

class NewtonForward(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "powder blue")   

        def setx():
            global xValueNewton
            """ it will take x values and y values 
             user has to enter values seperated by comma to create an array"""
            
            try:
                xValueNewton = entryXValues.get().split(",")
                xValueNewton = [float(x) for x in xValueNewton]
              # to check if the value return
                mb.showinfo("X Values:", xValueNewton)
            except ValueError:
                mb.showwarning('Wrong input', 'value is not valid')
                entryXValues.focus_set()
                return 

        def sety():
            global yValueNewton
            global valueNewtonX
            global table


            try:
                yValueNewton = entryYValues.get().split(",")
                yValueNewton = [float(x) for x in yValueNewton]
                
                table = [[0 for i in range(len(yValueNewton))]
                            for j in range(len(yValueNewton))]  
                for i in range(len(yValueNewton)):
                    table[i][0] = yValueNewton[i]
                mb.showinfo("Y Values:", yValueNewton)
            
            except ValueError:
                mb.showwarning('Wrong input', 'value is not valid')
                entryYValues.focus_set()

            try:
                xpNewton= entryZValues.get()
            except ValueError:
                mb.showwarning('Wrong input', 'Value entered is not valid')
                entryZValues.focus_set()
                return

        
        

        def button_pressed():  
            setx()
            sety()
            answer = fc.newton_forward(xValueNewton,table,xpNewton)
            mb.showinfo('yp value: ', answer, parent = self)

            f = Figure(figsize=(5,5), dpi = 100)
            a = f.add_subplot(111)
            a.plot((xValueNewton +[xpNewton]),(yValueNewton+[int(answer)]),'ro',(xValueNewton +[xpNewton]),(yValueNewton+[int(answer)]), 'b-')

            canvas = FigureCanvasTkAgg(f, self)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
            toolbar = NavigationToolbar2Tk(canvas, self)
        
            toolbar.update()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

  
        


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

        labelZ= Label(self, text = "Value that needs to be found: ", bg = "black", fg = "white")
        labelZ.config(font=("Courier", 11))
        labelZ.pack()

        entryZValues = Entry(self, width = 30, bg = "white")
        entryZValues.pack()

        button2 = Button(self, text = "The value of Y is: ", bg = "black", fg = "white", width = 30, command = button_pressed)
        button2.pack(padx = 10, pady = 5)
        button2.config(font=("Courier", 12))

        
        buttonMain = Button(self, text = " Main Menu", bg = "white", fg = "black", width = 25, command = lambda: master.switchFrame(mainMenu))
        buttonMain.pack(padx = 10, pady = 5)
        buttonMain.config(font=("Courier", 12))     

class NewtonBackward(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "powder blue")   

        def setx():
            global xValueNewton
            """ it will take x values and y values 
             user has to enter values seperated by comma to create an array"""
            
            try:
                xValueNewton = entryXValues.get().split(",")
                xValueNewton = [float(x) for x in xValueNewton]
              # to check if the value return
                mb.showinfo("X Values:", xValueNewton)
            except ValueError:
                mb.showwarning('Wrong input', 'value is not valid')
                entryXValues.focus_set()
                return 

        def sety():
            global yValueNewton
            global valueNewtonX
            global table


            try:
                yValueNewton = entryYValues.get().split(",")
                yValueNewton = [float(x) for x in yValueNewton]
                
                table = [[0 for i in range(len(yValueNewton))]
                            for j in range(len(yValueNewton))]  
                for i in range(len(yValueNewton)):
                    table[i][0] = yValueNewton[i]
                mb.showinfo("Y Values:", yValueNewton)
            
            except ValueError:
                mb.showwarning('Wrong input', 'value is not valid')
                entryYValues.focus_set()

            try:
                xpNewton= entryZValues.get()
            except ValueError:
                mb.showwarning('Wrong input', 'Value entered is not valid')
                entryZValues.focus_set()
                return

        
        

        def button_pressed():  
            setx()
            sety()
            answer = fc.newton_forward(xValueNewton,table,xpNewton)
            mb.showinfo('yp value: ', answer, parent = self)

            f = Figure(figsize=(5,5), dpi = 100)
            a = f.add_subplot(111)
            a.plot((xValueNewton +[xpNewton]),(yValueNewton+[int(answer)]),'ro',(xValueNewton +[xpNewton]),(yValueNewton+[int(answer)]), 'b-')

            canvas = FigureCanvasTkAgg(f, self)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
            toolbar = NavigationToolbar2Tk(canvas, self)
        
            toolbar.update()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
  
        


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

        labelZ= Label(self, text = "Value that needs to be found: ", bg = "black", fg = "white")
        labelZ.config(font=("Courier", 11))
        labelZ.pack()

        entryZValues = Entry(self, width = 30, bg = "white")
        entryZValues.pack()

        button2 = Button(self, text = "Calculate the value of Y: ", bg = "black", fg = "white", width = 30, command = button_pressed)
        button2.pack(padx = 10, pady = 5)
        button2.config(font=("Courier", 12))
        
        buttonMain = Button(self, text = " Main Menu", bg = "white", fg = "black", width = 25, command = lambda: master.switchFrame(mainMenu))
        buttonMain.pack(padx = 10, pady = 5)
        buttonMain.config(font=("Courier", 12))

    #newton

xValue = []
yValue = []
xp = 0

xValueNewton = []
yValueNewton = []
valueNewtonX = 0
xpNewton = 0

sizexNewton = len(xValueNewton)
sizeyNewton = len(yValueNewton)
table = []
   



if __name__ == "__main__":
    app = Interpolation()
    app.mainloop()