# printing 10 natural number in reverse order
x=int(input("enter the value how many natural number you want to in return order  :"))
while x!=0:
    if x>=10:
        print(" the {}th natural number is :".format(x),x)
    else:
        print(" the {}st natural number is  :".format(x),x)
    x-=1

