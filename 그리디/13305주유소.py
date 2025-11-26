n=int(input())
dist=list(map(int,input().split())) #i에서 i+1로 가는데 거리
cost=list(map(int,input().split())) #dist[i]=i에서 기름채우는 비용
total_cost=0
fuel_idx=0 #기름 넣을 주유소 위치

#현재 주유소보다 저렴한 주유소가 나올때까지 갈 수 있을만큼만 기름 넣고 이동한다
#저렴한 주유소가 나오면 비용을 변경한다
"""
4
2 3 1
5 2 4 1
"""
for pos in range(n-1):#pos: 012
    total_cost+=dist[pos]*cost[fuel_idx]
    if cost[fuel_idx]>=cost[pos+1]:
        fuel_idx=pos+1 #기름 넣을 주유소 위치 변경

print(total_cost)

