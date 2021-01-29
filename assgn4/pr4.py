#printing the prime no between  range of two values
x=int(input("enter the lower bound range for finding the prime no in that range : "))
y=int(input("enter the upper bound range for findng the prime no in that range  : " ))
count=0
if x<=1 or y<=1:
    print("please enter the values greater than 1")
    exit()
for a in range(x,y+1):
    n=a
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        print("prime no :",n)
        count+=1
print("Prime NO between {} and {} is : ".format(x,y),count)

