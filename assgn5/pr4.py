#print the squares of the numbers between the range
x=int(input("enter the value of lower bound of the range :"))
y=int(input("enter the value of upper bound of the range  :"))
for x in range(x+1,y):
    print(f"square of {x} is  ",x**2)

