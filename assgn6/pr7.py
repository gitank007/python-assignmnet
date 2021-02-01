#  find the occurange of elements in the list 
l=[int(x) for x in input("enter the list elements in one go with space  :").split()]
flag=[]
for i in range(len(l)):
        flag.append(0)
l.sort()
for i in range(len(l)):
    count=0
    if flag[i]!=1:
        for j in range(len(l)):
            if l[i]==l[j]:
                count+=1
                flag[j]=1
        print(f"the occurnace of integer {l[i]} : {count} ")
    else:
        continue



