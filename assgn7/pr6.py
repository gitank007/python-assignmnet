# string word sorting 
x=input()
# methode 1 using the list 
l=[i for i in x.split()]
l.sort()
print(*l,sep=' ')

# methode 2: using the loop
l1=[]
for i in x.split():
    l1.append(i)
    #print(i)
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[j]<l1[i]:
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
print(*l1,sep=" ")







