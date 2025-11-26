"""
https://kk-yy.tistory.com/49

"""

n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

dp=[0]*101

dp[0]=array[0]
dp[1]=max(dp[0],array[1])
for i in range(2,n):
    dp[i]=max(dp[i-1],dp[i-2]+array[i])

print(dp)

print(dp[n-1])
