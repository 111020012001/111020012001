def length(num):
    leng=0
    while num!=0:
       leng+=1
       num=num//10
    return leng
num=int(input("enter a number:"))
temp=num
rem=sum=0

len=length(num)
while num>0:
    rem=num%10
    sum=sum+int(rem**len)
    num=num//10
    len-=1

if sum==temp:
    print("it is a disarium number")
else:
    print("no it is not a disarium no.")
