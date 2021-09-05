def calculate_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for num in range(1,smaller+1):
        if x%num==0 and y%num==0:
            hcf=num
    return hcf

x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=calculate_hcf(x,y)
print("HCF of",x,"and",y,"is:",z)