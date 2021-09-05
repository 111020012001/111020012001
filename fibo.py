terms=int(input())
a=0
b=1
count=0
if terms<=0:
    print("try again")
elif terms==1:
    print(a)
else:
    while(count<terms):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
        count+=1
