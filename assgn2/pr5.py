# FIND THE GREATEST AMONG THREE NUMBER 
x=int(input("enter the first number :  "))
y=int(input("enter the second number :  "))
z=int(input("enter the thrid number:   "))
if x>y>z:
    print("The greatest among the three number is ",x)
elif x>z>y:
    print("The  gteatest  number among them is ",x)
elif y>x>z:
    print("The greatest number among the three of them is ",y)
elif y>z>x:
    print("The greatest number among them is ",y)
elif z>x>y:
    print("The greatest number among the given {} ,{} ,{} is ".format(x,y,z),z)
elif z>y>x:
    print("The greatest number amoung the given number is ",z)


#second methode using the list
numb=[int(numb) for numb in  input("enter the number:  ").split()]
numb.sort()
print("The greatest number is ",numb[2])

#or else  we can do is  using packing and unpacking we can doit 
a=[x,y,z]
a.sort()
print(a[len(a)-1])


