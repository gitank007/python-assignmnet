#caluclting the sum of first N natural no
N=int(input("Enter  the value of Natural number for upto which you want to calculate the sum : "))
temp=N
count=0
while N:
    count+=N
    N-=1
print("The sum of  the first {} natural naumber is :".format(temp),count)

