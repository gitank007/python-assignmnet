x=int(input("enter the value from which you want to revers printing of first x even no "))
x=2*x+1
count=0
for i in range(x,1,-2):
    print(i,end=" ,")
    count+=1
    print(count)

