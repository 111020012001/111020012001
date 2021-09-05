def recur_fact(n):
    if n==1:
        return n
    else:
        return n*recur_fact(n-1)
num=int(input("enter a number:"))
if num<=0:
    print("enter a valid number")
else:
    print(recur_fact(num))
