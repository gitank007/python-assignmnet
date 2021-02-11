# program to reverse the tupele :
# tuple_taking_inp
def tuple_inp():
    print("The Global tuple input for all of the mehodes of the program :")
    inp=eval(input())   # creating the global python function for taking the input as the 
    return inp          #tuple while implemneting the different events we just call the fun   
#x=tuple_inp()
#print(x)

#methode 1
inp1=tuple_inp()
l2=[]
print("This is methode 1 using the loops :")
rev_itr_var=len(inp1)-1
while rev_itr_var!=-1:
    l2.append(inp1[rev_itr_var])
    rev_itr_var-=1
print(tuple(l2))
# metode 2  using for loop and range function 
inp2=tuple_inp()
l3=[]
print("this is methode 2 using the for loop and range function  :")
for i in range(len(inp2)-1,-1,-1):
    l3.append(inp2[i])
print(tuple(l3))


#methode 3 using the list and using the list reverse methdoe and converted back using the tuple constructor
inp3=tuple_inp()
print("This is methode 3 using list and list reverse and converted back with tuple constructor:")
l1=list(inp3)
l1.reverse()
print (tuple(l1))

# methode 4: using the slicing opeartor 
inp4=tuple_inp()
print("the methdoe 4 using  the slicing opearator ;")
print(inp4[::-1])

# methode 5: using the loops with the slicing opearator   # pleSE SOLVE THIS ERROR TYPE OBJECT IS NOT SUBSTIPTABLE
#t=()                                                         
#for i in inp4[len(inp4)-1::-1]:
 #   t+i
#print(t)


