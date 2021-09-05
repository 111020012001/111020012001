def hapno(num):
    sum=0
    rem=0
    while(0 < num):
        rem=num%10
        sum=sum+rem*rem
        num=num//10
    return sum
nmu=int(input("enter a number:"))
result=num
while(result!=1 and result!=4):
    result=hapno(result)
if(result==1):
    print(str(num)+" is a happy no" )
elif(result==4):
    print("it is not a happy number")