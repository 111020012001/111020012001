def calculate_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    return lcm

x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=calculate_lcm(x,y)
print("LCM of",x,"and",y,"is:",z)