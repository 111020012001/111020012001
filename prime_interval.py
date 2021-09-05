lwr=int(input("enter lower range:"))
upr=int(input("enter upper range:"))
for num in range(lwr,upr+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
