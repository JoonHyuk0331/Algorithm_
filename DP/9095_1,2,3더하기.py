"""
점화식이 반드시 a+b=c인 경우는 없다는 점을 명심하기
"""

n=int(input())
dp=[0]*12

def sol(n):
    dp[1]=1
    dp[2]=2
    dp[3]=4
    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[n])

for _ in range(n):
    sol(int(input()))