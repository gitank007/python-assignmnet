#MERGINGING TWO SORTED TUPLE :
t1=eval(input("insert the values in the  first tuple :"))
print(type(t1))
print("printing the intial tuple :",t1)
t11=sorted(t1)
print(f"the sorted tuple is : {t11} ")
t2=eval(input("insert the values in the second tuple :"))
print(type(t2))
print(f"the scond tuple as entered by the user : {t2}")
t21=sorted(t2)
print(f"printing the second after sorting :{t21}  ")
print("Merging the two tuples into a single tuple  :")
t3=t11+t21  # mergiing two tuple
print(f"merging the tuple and noted that it simply insert the new elements with a new tuple : {t3}")
t3=sorted(t3)
print(f"the final sorted List is : {t3}")


