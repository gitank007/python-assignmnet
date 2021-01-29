# printing the first N natural odd number in reverse order usig range fuction 
x=int(input("enter the value of N"))
count=0
x=2*x-1
for i in range(x,0,-2):
    print(i,end=" ,")
    count+=1
    print(" ",count)
