#finding the year is leap year or no then it is a leap year otherwise not '''
x=int(input("enter the year you want to check for that it is a leap year or not :   "))
if ((x%4==0 and x%100!=0) or x%400==0):
    print("Leap year")
else:
    print("NOt a leap Year:")
    
