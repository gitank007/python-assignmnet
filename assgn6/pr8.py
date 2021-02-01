x=int(input("enter the numers in the list"))
l=[]
for i in range(1,x+1):
    l.append(i)
print("the given list is ",*l)
def evenodd(l):
    evensum=0
    oddsum=0
    for i in l:
        if i&1==0:
            evensum+=i
        else:
            oddsum+=i
    print("the sum of the even no's in the list is   : ",evensum)
    print("the sum of add no's present in the list is : ",oddsum)
evenodd(l)

