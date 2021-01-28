#methde 1 to compare three string
print("Enter three string ")
x,y,z=input(),input(),input()
if x<y<z:
    print(x,y,z)
elif x<z<y:
    print(x,z,y)
elif y<x<z:
    print(y,x,z)
elif y<z<x:
    print(y,z,x)
elif z<x<y:
    print(z,x,y)
else:
    print(z,y,x)

# methode 2 using the min max function 
print("enter three words")
x,y,z=input(),input(),input()
a=min(x,y,z)
print(a,end=" ")
if x==a:
    print(min(y,z),max(y,z))
elif y==a:
    print(min(x,z),max(x,z))
else:
    print(min(x,y),max(x,y))
#methode 3
# using the for in complex list
[x for x in sorted(input("enter the given Words in space seprated pattern :").split()) if print(x,end=" ")]
