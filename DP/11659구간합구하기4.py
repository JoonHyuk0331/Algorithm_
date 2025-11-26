"""
d[i]=d[i-1]+arr[i]
m이 최대 100000 이므로 input() 시 시간초과가 발생할 수 있음
라인 17 perfix sum 기억해두기
"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

d=[0]*(n+5)
d[1]=arr[0]

for i in range(2,n+1):
    d[i]=d[i-1]+arr[i-1]

for i in range(m):
    a,b=map(int,input().split())
    print(d[b]-d[a-1]) #perfix sum 기법