# CHECCKING FOR THE PALINDORME
#METHODE1
def ispalindrome(a,b):
    if a==b:
        print("Yes Plandrome Becsuse reversal  of the string is same as the input string  :")
    else:
        print("NO the given string is Not a PlainDrome because the Reversal is Not eqaul to the Given String :")

string_input=input()

rev_string=string_input[::-1]

ispalindrome(string_input,rev_string)

#methode 2:
x=""
for i in range(len(string_input)-1,-1,-1):
    x+=string_input[i]
#print(x)
ispalindrome(string_input,x)

#methode3
l=list(string_input)
l.reverse()
reversal_using_list=''
for i in l:
    reversal_using_list+=i
ispalindrome(string_input,reversal_using_list)







