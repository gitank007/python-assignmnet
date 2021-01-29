y=int(input("enter the value for which you want calculte the prime factor  :"))
for a in range(2,y):
    if y%a==0:
        x=a
        #x=int(input("enter the value for which you want to find the prime factor"))
        if x<=1:
            print("please enter another value:")
        else:
            flag=0
            for i  in range(2,x):
                if x%i==0:
                    flag=1
                    break
            if flag==0:
                print("prime factor",x)




