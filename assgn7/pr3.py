 # revesing the string 
string=input("entering the string : ")
#using the list
l=[]
l=list(string)
l.reverse()
x=str(l)
print(x,"the list is as reveral using the list reveral\n",sep='')
str1=''
for i in  l:
    str1+=i
print(str1,'\n Now printed the converted from the list to string  using the for  loop and string concatination methode\n')

#direct methode to print the list withouht quotes even if you remove the sepraters it will print as it as string reversal 
print(*l,sep='')
print("printed using the * operator at once  in go  :")

#methode 2
for i in range(len(string)-1,-1,-1):
    print(string[i],end="")
print("\n")

#best_methode to reverse the string
x=string[::-1] #reversing the string using the slicing opearator
print(x)
