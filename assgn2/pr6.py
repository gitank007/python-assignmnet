x=int(input("enter the month number  :"))
if x==1:
   print("January has  31 days ")
elif x==2:
    print("feburary has 29 or 28 days")
elif x==3:
    print("march has 30 days")
elif x==4:
    print("april has 30 days :")
elif x==5:
    print("may has 31 days")
elif x==6:
    print("june has 30 days ")
elif x==7:
    print("july has 31 days ")
elif x==8:
    print("august has the 31 days ")
elif x==9:
    print("september has 30 days ")
elif x==10:
    print("october has 31 days ")
elif x==11:
    print("November  has 30 days ")
else:
    print("december has 31 days ")

#methode 2 using the calendar module 
import calendar
import sys
print("want to see calender of a month enter year then followed by month press 0 if dont intrested  :")

z=int(input("enter the choice  "))
if z==0:
    sys.exit()
else:
    year=int(input("enter the year "))
    month=int(input("enter the month"))
    print(calendar.month(year,month))
