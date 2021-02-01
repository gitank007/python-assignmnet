# program to count the no of vowels in the program 
def vowel(string):
    count=0
    for i in string:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
        else:
            continue
    return count
string=input("enter the iput string in which you want to count the no of the vowel's  :")
print(f"NO's of the Vowel's present in the string '{string}'  is  :{vowel(string)} ")

