# finding the given pattern is present in the string or Not

# methode 1 ... > using the index 
a=input("enter the given string :")
b=input("enter pattern you want to find  :")
if a.index(b)==0:
     print("Yes it is Present in The given string")
elif a.index(b):
     print("Yes the Given Pattern is present in the string")
else:
    print("The given string is Not present in the strign :")


# methode 2 using the membership operaotr
x=input("enter the sting ")
y=input("enter the pattern you want to find :")
if y in x:
    print("yes the gievn pattern is present in string :")
else:
    print("The given pattren is not present in the given strin g ;")


# methode 3  using loops 
c=input("enter the given string:")
d=input("enter the pattern you want to find :")
i=0
j=0
while j<len(c):
    if d[i]==c[j]:
        i+=1
        j+=1
        if i==len(d)-1:
            print("Yes the given pattern is present in the given string :")
            i=0
            break
    else:
        i=0
        j+=1
else:
    print("The given pattern is NOt present in the given string :")
