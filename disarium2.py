def cal_len(n):
    l=0
    while n!=0:
        n//=10
        l+=1
    return l
def sum_of_digits(num):
    digit=sum=0
    len=cal_len(num)
    while num>0:
        digit=num%10
        sum=sum+int(digit**len)
        num//=10
        len-=1
    return sum

res=0
for i in range(1,101):
    res=sum_of_digits(i)
    if res==i:
        print(i,end=" ")







