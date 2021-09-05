def recur_fibo(n):
    if n<=1:
        return n
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))
nterms=int(input("enter terms:"))
if nterms<=0:
    print("please enter a positive number")
else:
    print("fibonacci sequence")
    for i in range(nterms):
        print(recur_fibo(i),end=" ")
