# finding the count of a character in the string 
string_inp=input( "enter the string : ")
srch_char=input("enter the charcter you want to search  :")

#methode 1
count=0
for i in string_inp:
    if i==srch_char:
        count+=1
print(count)

#methode 2:using the count funtion 

print(string_inp.count(srch_char))

