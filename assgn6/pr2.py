l=[int(x) for x in input("enter the list elements :").split()]
print(l)

#methode `
print(max(l),"methode 1")
#methode 2
x=list(l)
l.sort()
print(l[len(l)-1],"methode 2") # methode 2 another way using simple basic 2 for loop to iterate over and sort w/o using the sorting 

#methde3  using the max named  variable and updating and printing at the last 
maximum=0
for i  in  x:
    if maximum<i:
        maximum=i
    else:
        continue
print(maximum,"methode 3")


