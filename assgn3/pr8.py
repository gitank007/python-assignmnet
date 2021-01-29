# caluclate the sum of first N natural odd NUmber 
x=int(input("Enter the  value of odd Natural number whose sum you wan to calculte : "))
temp=x
T=x
x=1
count=0
while T:
    if x%2!=0:
        count+=x
        x+=1
        T-=1
    else:
        x+=1
print("The sum of first {} natural odd number is : ".format(temp),count)

