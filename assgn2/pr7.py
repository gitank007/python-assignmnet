''' nature of roots 
step 1: if d=b^2 -4ac =0 ==>real and equal roots
step 2 if d>0 then they are rel  roots 
step 3 if d<0 then it is imaginary rots 
'''
x,y,z=[int(x) for x in input("enter the space seprating values of cofficients of ax^2+bx+c values will be considered in repective manner: ").split()]
print("a={} ,b={}, c={} ".format(z,y,z))
d=(y**2)-4*x*z
print("the Value of discriminant for given equation is :",d)
if d==0:
    print("The roots are real and equal ")
elif d>0:
    print("The roots are real ")
else:
    print("The rots are imaginary ")

