#displaing the student is pass or fail by taking the input of   5 subject if pass also display the % and grade
x,y,z,a,b=[int(z) for z in input("enter the marks using space ").split()]

l=x,y,z,a,b
sum=0
for x in l:
    if x<33:
        print("fail :","The garde of the student is : F ")
        
        import sys
        sys.exit()
    else:
        sum+=x
if sum >=500:
    print("The marks entered by  the opearator is wrong :")
    import sys
    sys.exit()
marks=sum/5        
print("marks stored by the candidate is: ",marks,"%")
if (marks<50):
    print("and grade of the student is : c ")
elif marks<60 and marks >=50:
    print("The grade of the student is : c+")
elif marks <70 and marks >=60:
    print("The grade of the studnet is   : B")
elif marks <80 and marks >=70:
    print("The grade of the student is  : B+")
elif marks <90 and marks >=80 :
    print("The grade of the student is   :A:")
elif marks <100 and marks >=90:
    print("The grade of the student  is  : A+")
else:
    print("The student is get perfect 100 %:")

# methode 2 using simple methode 
x=int(input("enter the first subject marks "))
y=int(input("enter the second subject marks "))
z=int(input("enter the third subject marks "))
m=int(input("enter the fourth subject marks "))
n=int(input("enter the fifth subject marks "))
l=[x,y,z,m,n]
sum=0
for x in l:
    if x<33:
        print("fail :","The garde of the student is : F ")
        import sys
        sys.exit()
    else:
        sum+=x
if sum>=500:
    print("marks entered by the operaor is wrong please check again ")
    import sys
    sys.exit()
else:
    marks=sum/5
    print("marks stored by the candidate is: ",marks,"%")
    if (marks<50):
        print("and grade of the student is : c ")
    elif marks<60 and marks >=50:
        print("The grade of the student is : c+")
    elif marks <70 and marks >=60:
     print("The grade of the studnet is   : B")
    elif marks <80 and marks >=70:
        print("The grade of the student is  : B+")
    elif marks <90 and marks >=80 :
        print("The grade of the student is   :A:")
    elif marks <100 and marks >=90:
        print("The grade of the student  is  : A+")
    else:
        print("The student is get perfect 100 %:")

