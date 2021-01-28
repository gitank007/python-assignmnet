#simple intrest is s.i.=prncpl*rate*time/100
prncpl=float(input("enter the priciple amnt"))
rate=float(input("enter the rate of the intreset"))
time=float(input("please enter the year for which you had to claculate the intreset"))
'''if it is in month please convert that to into the year by dividing them into 12 like as 
 time =6 month
 so it should be coverted as 6/12=0.5 year
 '''
s_i=prncpl*rate*time/100
print("simple intrest of  {} for {} at an rate of {} is {} ".format(prncpl,time,rate,s_i))

