#바텀업 방식으로 i번째 계단을 밟았을때 지금까지 최대 점수를 누적하며 올라가면 될듯
"""
https://daimhada.tistory.com/181
어디로 올라갈까 가 아니라
어디에서 올라왔나에 포커스를 맞추자

첫번째 두번째가 채워진 dp리스트에서 세번째를 어떻게 만족할지 찾아보자

가능한 경우의 수 조합에서 점화식을 유추하자
세칸을 연속해서 올라갈 수 없으므로 5번째 계단으로 올라올 수 있는 경우의 수는
1345 2345 245 35 45 인데 세칸을 연속해서 올라갈 수 없으므로 45 35만 가능
이떄 45일 경우 345가 될수 없으므로 245
따라서 최소단위로 떨어지는 경우의 수는 35 245
따라서 +2칸 또는 +2,+1칸 올라가는 경우의 수로 모든 올라가는 패턴을 표현 가능하다
이를 참고하여 점화식을 만들었다
"""

n=int(input())
stairs=[]
for _ in range(n):
    stairs.append(int(input()))
dp=[0]*n

if n==1:
    print(stairs[0])
elif n==2:
    print(stairs[0]+stairs[1])
else:
    dp[0]=stairs[0]
    dp[1]=stairs[0]+stairs[1]
    dp[2]=max(stairs[2]+dp[0],stairs[2]+stairs[1])
    for i in range(3,n):
        two=stairs[i]+dp[i-2]
        two_one=stairs[i]+stairs[i-1]+dp[i-3]
        dp[i]=max(two,two_one)
    print(dp[-1])