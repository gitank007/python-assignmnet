#counting the elements in the tuple :using  the 
#methode 1 using the count funtion 
print("For entering the string please use double qoutes :")
tup=eval(input())
print("enter the elements you you want to count :")
a=eval(input())
b=tup.count(a)
print(b)

# methode 2 : using the if  condition and counting 
count=0
tup1=eval(input("enter the tuple elements are :"))
print("enter the tuple element you want to search  :")
se_input=eval(input())
for i in tup1:
    if se_input==i:
        count+=1

print(count)



