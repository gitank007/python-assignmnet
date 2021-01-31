x=int(input("enter the size of the list "))
l=[]
sum=0
for i in range(x):
    l.append(int(input()))
    sum+=l[i]
print(sum)
