import math

def factorial(num):
    if num==1:
        return 1
    else:
        return (factorial(num-1)*num)//10**8


for i in range(int(input())):
    s,*temp=input().split()
    n,t,l=map(int,temp)
    time=0
    if s=='O(N)':
        time=n
    elif s=='O(2^N)':
        time=2**n
    elif s=='O(N!)':
        if n>12:
            print("TLE!")
            continue
        time=math.factorial(n)
    elif s == 'O(N^2)':
        time=(n**2)
    elif s=='O(N^3)':
        time=(n**3) #자릿수 너무 커질듯

    if time*t<=l*10**8:
        print("May Pass.")
    else:
        print("TLE!")