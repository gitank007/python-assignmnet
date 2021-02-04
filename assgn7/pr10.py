# program for counting the no of pattern in a string  ---:>>
#methode 1


a=input()
b=input()
l2=list(a)
l3=list(b)

i=0
count=0
for j in range(0,len(l2)):
    if l3[i]==l2[j]:
        i+=1
        j+=1
        if i==len(l3)-1:
           # print("Yes")
           # print("index of the b in the is string is : ",(a.index(b)))
            count+=1
            i=0
    else:
        i=0
        j+=1
print(count)


#methode 2 for counting the pattern in the string ...    ----- >>

c=input("enter the string in which you want to  find :")
d=input("enter the pattern you want to search  :")
i=0
j=0
count=0
while j<len(c):
    if d[i]==c[j]:
        i+=1
        j+=1
        if i==len(d)-1:
            count+=1
            i=0
    else:
        i=0
        j+=1
print("\n COUNTING THE PATTERN BY THE SECOND METHODE ",(count))


#methode 3 smallest methode to count the no of times of a string has that pattern

j_string_input=input("enter the string :")
k_search_pattern=input("enter the pattern you want to search  :")
l_sep_string=j_string_input.split(k_search_pattern)
print(f"the count of the pattern in the string is : {len(l_sep_string)-1} ")


#methode 4 using the count inbuilt methode  methode 
f_input=input()
g_input=input()
print(f_input.count(g_input))
