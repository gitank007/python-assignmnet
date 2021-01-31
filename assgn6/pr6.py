#finding the index of the list of the common words 
l=[(int(x)) for x in input("enter the list of the elements :").split()]
y=int(input("enter the elemets you want to search "))
for i in range(len(l)):
    if l[i]==y:
        print(i)

#other methode to solve is if you find and index return it and remove  that and again search

