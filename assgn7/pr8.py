# wrintg the program to delete the duplicate charcters from the string :
print("enter the string w/0 putting space in in ")
flag=[]
l1=input()
for i in range(len(l1)):
    flag.append(0)
x=''
for i in range(len(l1)):
    if flag[i]==0:
        x+=l1[i]
        for j in range(len(l1)):
            if l1[j]==l1[i]:
                flag[j]=1
print(x)

#methode 2 using the function 
x=''
def NO_repaet(y):
    flag=[]
    l1=list(y)
    for i in range(len(l1)):
        flag.append(0)
    for i in range(len(l1)):
        if flag[i]==0:
            global x
            x+=l1[i]
            for j in range(len(l1)):
                if l1[j]==l1[i]:
                    flag[j]=1
string_input=input("enter the repeative string : ")
l=list(string_input.split())
for i in l:
    y=i
    NO_repaet(y)
    x+=' '
print(x)
