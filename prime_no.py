def primeCheck(num):
    if num>1:
        for j in range(2,int(num/2)+1):
            if(num%j)==0:
                print("not a prime no")
            else:
                print("prime no")
    else:
        print("not a prime no")
num=int(input())
primeCheck(num)