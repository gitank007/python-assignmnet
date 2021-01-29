y=int(input("enter the lower range for which you want to calculate the armstroang no : "))
for x in range (y+1):
    temp=x
    sum=0
    digit=0
    while x!=0:
        digit=x%10
        sum+=(digit**3)
        x=x//10
    if temp==sum:
        print("Armstrong Number is ",temp)

