import numpy as np
from functions import u_cal_backward
from functions import factorial
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

arr=create_array(4)
print(arr)

yarr=create_yvalues_table(4)
print(yarr)

print(newton_backward(arr,yarr,1.7))


