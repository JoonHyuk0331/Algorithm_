n=int(input())
costs=[]
dp=[[0]*3 for _ in range(n)]
for _ in range(n):
    costs.append(list(map(int,input().split())))

for c in range(3):
    dp[n-1][c]=costs[n-1][c]

for i in range(n-2,-1,-1): #n-2~0
    for c in range(3): #rgb 012에 대한 dp 찾기
        others=[0,1,2]
        others.remove(c)
        #컬러에 해당하지 않는 dp값중 최솟값찾아 costs[i]값과 더하기
        min_cost=999999
        for other in others:
            min_cost=min(min_cost,dp[i+1][other])
        dp[i][c]=min_cost+costs[i][c]

print(min(dp[0]))