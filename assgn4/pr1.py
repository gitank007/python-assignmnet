x=int(input("ENter the number you want  to check either prime or not : "))
flag=0
for i in range(2,x):
    if x%i==0:
        flag=1
        break
if flag==0:
    print("Prime No")
else:
    print("Not a prime NO")


