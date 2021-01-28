#dipslcing the greater part of complex no between real part and imaginary part 
x=complex(input("enter the complex no in terms of a+bj where j is the imaginary part: "))
if x.real>x.imag:
    print(x.real)
else:
    print(x.imag)
