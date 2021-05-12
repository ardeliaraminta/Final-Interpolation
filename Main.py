import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import ( FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk


class Interpolation(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Interpolation ")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (mainMenu, Introduction, Langrange, Newton):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(mainMenu)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class mainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Computational Mathematics", font=fixed_font)
        label['bg'] = 'blue'
        label['fg'] = 'white'
        label.pack(pady = 50, padx = 30)

        label2 = tk.Label(self, text = " by Rohan, Raphael, Ardelia")
        label.pack(pady=10,padx=10)
        label2.pack(pady=20, padx= 20)

        button = ttk.Button(self, text=" Interpolation",command=lambda: controller.show_frame(Introduction))
        button.pack()

        button2 = ttk.Button(self, text="Langrange",command=lambda: controller.show_frame(Langrange))
        button2.pack()

        button3 = ttk.Button(self, text="Newton Forward Interpolation",command=lambda: controller.show_frame(Newton))
        button3.pack()


class Introduction(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Introduction", font=fixed_font)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Main", command=lambda: controller.show_frame(mainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Langrange",command=lambda: controller.show_frame(Langrange))
        button2.pack()


class Langrange(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Langrange", font=fixed_font)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Main",command=lambda: controller.show_frame(mainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",command=lambda: controller.show_frame(Introduction))
        button2.pack()


class Newton(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Newton ", font=fixed_font)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Main",command=lambda: controller.show_frame(mainMenu))
        button1.pack()
 

 
fixed_font= ("Times New Roman", 12)

app = Interpolation()
app.mainloop()