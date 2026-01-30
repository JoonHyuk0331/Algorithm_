"""
딱~ 봐도 dp아닙니까

1.메모리 초과 문제로 나누기 연산이 주어지는 경우 결과에다가만하면 의미 없다
각 배열에 큰 숫자가 들어가지 않게 하기 위함이기 때문

2.시간초과 시, sys.stdin.readline 의심

3.매번 계산하지 말자
"""
import sys
input = sys.stdin.readline
t=int(input())

dp = [0]*191230
dp[1]=1
dp[2]=2
for i in range(3,191230):
    dp[i]=(dp[i-1]+dp[i-2])%(10**9+7) # 계산할때마다 나누기연산
for _ in range(t):
    print(dp[int(input())])



