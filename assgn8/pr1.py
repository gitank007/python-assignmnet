#methode 1 entering  the touple from user input to calculte the average
t=eval(input())
sum=0
for i in t:
    sum+=i
print(f"the sum of the given tuple is : {sum}")
print(f"The average of the given Tuple is :{sum//len(t)})")

#methode 2 using the simple input() funtion 
t1=tuple(input())
sum1=0
for i in t1:
    sum1+=int(i)
print(f"the sum of the give tuple  is :{sum1}")
print(f"the average of the given tuple is :{sum1//len(t1)}")

