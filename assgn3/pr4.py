# printing first 10 natural no 

x=10
y=1
count=1
while x:
    if y%2==0:
        print("the {}st eevn no is ".format(count),y)
        x-=1
        count+=1
        y+=1
    else:
        y+=1

