import sys
input=sys.stdin.readline

dp=[0]*10001
dp[1]=1

for i in range(2,10001):
    a=(i+4)//6
    if i%6==0:
        a+=1
    dp[i]=dp[i-1]+a

for _ in range(int(input())):
    print(dp[int(input())])