# caluclate the lcm and hcf of the two number 
''' gcd*lcd=a*b
   using this we get ==> lcm=(a*b)//gcd
   '''
x=int(input("enter the first number for which you want to calculte the lcm  :  "))
y=int(input("ente  the second number for which you want to calculte the lcm :  "))
def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x
hcf=(gcd(x,y))
#print("lcm=(a*b)//(gcd))")
lcm=(x*y)//hcf
print(f"the lcm of the given no {x,y} is {lcm}")



