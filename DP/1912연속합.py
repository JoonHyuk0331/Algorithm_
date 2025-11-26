"""
점화식 찾기가 쉽지 않았던 문제

지금까지 더한 합에 현재값을 더한게 현재 값보다 크지 못하면 지금까지 더한 값은 필요가 없다는 아이디어
"""
n=int(input())
li=list(map(int,input().split()))
dp=[0]*n # 빈리스트에 어떤 수를 곱해도 빈 리스트임

dp[0]=li[0]
for i in range(1,n):
    dp[i]=max(li[i],dp[i-1]+li[i])
print(max(dp))