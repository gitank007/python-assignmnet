# print first 10 odd natural number
x=int(input("Enter the value of odd no you want to print "))
y=1
count=1
while x:
    if y%2!=0:
        print("THe {}st odd no is ".format(count),y)
        x-=1
        y+=1
        count+=1
    else:
        y+=1

