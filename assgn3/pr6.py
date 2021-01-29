# printing in revrese order 
x=int(input("enter the NOof natural numbes you want to print in reverse order "))
count=1
while x:
    if count>=10:
        print("The {}th Natural Number in reverse order is :".format(count),x)
        count+=1
        x-=1
    else:
        print("The {}st nautral Number in reverse order is :  ".format(count),x)
        count+=1
        x-=1

