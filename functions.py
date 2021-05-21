import numpy as np 
import tkinter as tk 
import matplotlib.pyplot as plt


#functions 

x =np.array([0, 20, 40, 60, 80, 100], float)
y =np.array([26.0, 48.6, 61.6, 71.2, 74.8, 75.2], float) 

xplt = np.linspace(x[0], x[-1])
yplt = np.array([], float)

for xp in xplt:
    yp = 0
    
    for xi,yi in zip(x,y): #iterator of array x and y 
        yp += yi * np.prod(( xp - x[x != xi]) / (xi - x[x != xi]))
    yplt = np.append(yplt,yp)

#print graph     
plt.plot(x,y, 'ro', xplt, yplt, 'b-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


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
    u = (x - xvalues[0]) / (xvalues[1] - xvalues[0])
    for i in range(1,n):
        ans = ans + (u_cal_forward(u, i) * yvalues[0][i]) / factorial(i)
  
    print("\nValue at", x, 
        "is", round(ans, 6)) 
    
        
def u_cal_backward(u,n):
    temp = u
    for i in range(1, n):
        temp = temp * (u + i)
    return temp

#for xvalues
def create_array(size):
   arr= np.array(size)
   for i in size:
       arr[i]=input("Enter value: ")
   return arr

# for yvalues
def create_yvalues_table(xvalues):
    y = [[0 for i in range(xvalues.size)]
        for j in range(xvalues.size)]
    for i in xvalues.size:
        y[i][0]=input("Enter value: ")
    return y
    
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

    
   

