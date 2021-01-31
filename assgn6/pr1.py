# PROGRAM TO SORT THE LIST w/O USING THRE SORT GIEN BY USER
x=int(input("enter the size of the list : "))
l=[]
for i in range(x):
    l.append(int(input("enter the elements of the list  : ")))
print(f"The list before sorting of the element is {l} ")
#y=int(input("if you to sort the list in asending order enter 1 otherwise for desending order enter any value   : "))
def asdelist(l):
    for i in range(x):
        for j in range(i+1,x):
            if l[j]<l[i]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
            else:
                continue
    return l
def desdorder(l):
    for i in range(x):
        for j in range(i+1,x):
            if l[j]>l[i]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
            else:
                continue
    return l

print(asdelist(l),"the list in asending order is ")
print(desdorder(l),"the list in desending order ")


    
