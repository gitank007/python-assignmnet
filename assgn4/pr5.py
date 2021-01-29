# find the greatest common divisor in simple and easy way 
x=int(input("Enter the first NUmber "))
y=int(input("enter the second number"))
min=x if x<y else y
max=x if x>y else y
hcf=1
#print(min," ", max)
for i in range(min,max+1):
    if (x%i==0 and y%i==0):
        hcf=i
        #print(hcf)
if hcf==1:
    print(f"{x,y} are co prime number ")
else:
    print(f"{x,y} are not co prime no as their  hcf is {hcf}")


##using the importing math 
import math 
x=int(input("enter the first number"))
y=int(input("enter the second number"))
m=math.gcd(x,y)
if m==1:
    print(f"the gcd of the {x,y} is 1 so they are co-prime  ")
else:
    print(f" the gcd of the {x,y} is {m} so they are not co-prime")

#methode 3 using the eculedian methode 
x=int(input("enter the first digit"))
y=int(input("enter the second digit "))
def gcd(x,y):
    if y==0:
        print(x)
    else:
        return gcd(y,x%y)
print(gcd(x,y))

#methode 4
x=int(input())
y=int(input())
def gdc(x,y):
    while y!=0:
        x,y=y,x%y
    return x
print(gdc(x,y))

