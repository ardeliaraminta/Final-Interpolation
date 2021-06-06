import numpy as np 
import tkinter as tk 
import matplotlib.pyplot as plt


#functions 

#linear 
def linear_interpolation(x0,y0,x1,y1,xp,yp):
    if yp==0:
        yp= y0 + ((y1-y0)/(x1-x0)) * (xp - x0)
        return yp
    elif xp==0:
         xp=(yp-y0)/((y1-y0)/(x1-x0))+x0
         return xp


##############################################################################################################################
#Newton

def create_xarray(size):
    # Making numpy array of n & n x n size and initializing 
    # to zero for storing x and y value along with differences of y
    x = np.zeros((size))
    # Reading data points
    print('Enter data for x: ')
    for i in range(size):
        x[i] = float(input( 'x['+str(i)+']='))
   
    return x


#for xvalues
def create_array(size):
   arr=[]
   for i in range(size):
       arr.append(eval(input("Enter value: ")))
   return arr

# for yvalues
def create_yvalues_table(size):
    y = [[0 for i in range(size)]
        for j in range(size)]
    for i in range(size):
        y[i][0]=eval(input("Enter value: "))
    return y


#calculating the value of u
def u_cal_forward(u, n):
  
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp

#calcualting factorial

def factorial(n):
    a=n
    for i in range(n-1,1,-1):
        a*=i
    return a

   
   
def newton_forward(xvalues,yvalues,x):
    n=len(xvalues)
    # Calculating the forward difference
# table
    for i in range(1, n):
        for j in range(n - i):
            yvalues[j][i] = yvalues[j + 1][i - 1] - yvalues[j][i - 1]
  
# Displaying the forward difference table
    for i in range(n):
        print(xvalues[i], end = "\t")
        for j in range(n - i):
            print(yvalues[i][j], end = "\t")
        print("")
    
    # initializing u and sum
    ans = yvalues[0][0]
    u = (int(x) - xvalues[0]) / (xvalues[1] - xvalues[0])
    for i in range(1,n):
        ans = ans + (u_cal_forward(u, i) * yvalues[0][i]) / factorial(i)
  
    return ans
    
        
def u_cal_backward(u,n):
    temp = u
    for i in range(1, n):
        temp = temp * (u + i)
    return temp

    
def newton_backward(xvalues,yvalues,x):
    n=len(xvalues)
    for i in range(1, n):
        for j in range(n - 1,i-1,-1):
            yvalues[j][i] = yvalues[j][i - 1] - yvalues[j - 1][i - 1]
    
    for i in range(n):
        print(xvalues[i], end = "\t")
        for j in range(0,i+1):
            print(yvalues[i][j], end = "\t")
        print("")

    ans=yvalues[n - 1][0]
    u = (x - xvalues[n - 1]) / (xvalues[1] - xvalues[0])
    for i in range(1,n):
        ans = ans + (u_cal_backward(u, i) * yvalues[n - 1][i])/factorial(i)
    
    print("Value at ", x, 
        " is ", round(ans, 6))


######################################################################################################
#Lagrange

def create_xarray(size):
    # Making numpy array of n & n x n size and initializing 
    # to zero for storing x and y value along with differences of y
    x = np.zeros((size))
    # Reading data points
    print('Enter data for x: ')
    for i in range(size):
        x[i] = float(input( 'x['+str(i)+']='))
   
    return x

def create_yarray(size):

    y = np.zeros((size))
    print('Enter data for y: ')
    for i in range(size):
        y[i] = float(input( 'y['+str(i)+']='))
    
    return y

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

    # Displaying output
    print('Interpolated value at %.3f is %.3f.' % (xp, yp))

    
   

