# check for even odd 
x=int(input("enter the number you want to check for eevn or odd: "))

#y=eval(input("enter the number you want to check the even or odd "))
if isinstance(x,int):
    if x==0:
         print("please enter the number greater than 0 :")
    elif x%2==0:
         print("The entered number by the user is a even no ")
    else :
         print("user entered a odd number ")
else:
    print("you have no entered a correct no  :",x)

#using eval function you can genrelised more 
y=eval(input("enter the number you want to check the even or odd "))
if isinstance(y,int):
    if x==0:
         print("please enter the number greater than 0 :")
    elif x%2==0:
         print("The entered number by the user is a even no ")
    else :
         print("user entered a odd number ")
else:
    print("you have no entered a correct no :",y)



