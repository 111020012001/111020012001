def NumberCheck(a):
    if a>0:
        print("number is positive.")
    elif a<0:
        print("number is negative.")
    else:
        print("number is zero.")
a= float(input("enter a value: "))
NumberCheck(a)