# to print the next prime no"
x=int(input("enter the value after you want to check the prime no: "))
while True:
    x+=1
    flag=0
    if x<=1:
        continue
    for i in range(2,x):
        if x%i==0:
            flag=1
            break
    if flag==0:
        print("The next prime No is ",x)
        break

