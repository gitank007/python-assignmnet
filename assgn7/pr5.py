#counting the no of times of a word 
strng_inp=input()
srch_inp=input()
#methode 1 using the list
l=[ i for i in strng_inp.split()]
count=0
print(l)

for i in l:
    if i==srch_inp:
        count+=1
print(count)

#methode2 using the count methode 
print(strng_inp.count(srch_inp))


