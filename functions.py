
x1 = [0,20,40,60,80,100]
y1 = [26,48.6, 64.3, 71.2, 74.8, 80.9]

m = len(x1)
n = m-1 #degree of polynomials 

xp1 = float(input("enter x: "))
yp1 = 0 

for i in range(n+1):
    p = 1
    for j in range(n+1):
         if j != 1:
             p += (xp1- x1[i]- x1[j] )
    yp1+= y1[i] * p


print(' for x = %.2f, y = %f' % (xp1,yp1))
