#demonstrate how to use the argv module to take the input directly w/0 running the  file in the command line 

from sys import argv
print("predefined sys module has argv inbuild varibale of list type having string value as defalut ")
print("using this we pass the argument to the program even withough running it by placing the argumnets in commond line in space seprated :")
print("pass the parameter in the same line of command line using space between two argument ")
y=0
sum=0
print("\n",argv)
for i in argv:
    print(type(i))
for i in argv:
    if y==0: # the value of y has been assigned to 0 bcz at the zeroth index it contins the filename itself we have to pass it intiallly
        y=1 # or we can say that we can run the loop from the 1 as we had done in the for convering each varible to final int type of whole
    else:
        sum+=int(i)
print("Now printing  the new sum of the eleements in the list intially all of the are string type by converting them into the int printing sum:")
print(sum)

print("converting their initial type str to int type usig for loop starting from index 1  : as index 0 has the filename itself ;.")
for i in range(1,len(argv)):
        argv[i]=int(argv[i])
for i in argv:
    print(type(i))


