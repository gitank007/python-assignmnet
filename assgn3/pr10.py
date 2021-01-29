# print the first multiplication of first N odd natural number
x=int(input("Enter the value to get product of first N odd no  :"))
#x=int(input("enter the value of N of odd number for which you want to get the multpliction "))
temp=1
count=1
mul=1
while count:
    if count%2!=0:
        mul*=count
        count+=1
        temp+=1
        if temp>x:
            break
        else:
            continue
    else:
        count+=1
print(mul)
