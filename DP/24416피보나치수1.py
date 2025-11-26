fibcnt=1
fibocnt=0

n=int(input())

def fib(n):
    global fibcnt
    if n==1 or n==2:
        return 1
    else:
        fibcnt += 1
        return fib(n-1)+fib(n-2)


d=[0]*100

def fibo(k):
    global fibocnt
    d[1]=1
    d[2]=1
    for i in range(3,k+1):
        fibocnt+=1
        d[i]=d[i-1]+d[i-2]

fib(n)
fibo(n)
print(fibcnt,fibocnt)