# printing first n natural number 
x=int(input(" Ente the number of naural nos you want to print  :"))
temp=1
while temp!=x:
    if x>=10:
        print("The {}th Naural Number is :".format(temp),temp)
        temp+=1
    else:
        print("The {}st Natural NUmber is :".format(temp),temp)
        temp+=1

    
