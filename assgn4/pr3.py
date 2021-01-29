# printing N prime NO {N is user input }
x=int(input("Enter the NO of time you print the prime NO  :"))
p=1
count=0
while True:
    flag=0
    p+=1
    for  i in range(2,p):
        if p%i==0:
            flag=1
            break
    if flag==0:
        count+=1
        print("Prime NO {} is ".format(count),p)
        if count==x:
            break
        else:
            continue


