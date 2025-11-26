from collections import deque

n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
m=int(input())
arr3=list(map(int,input().split()))

q=deque()
#큐인 경우에만 큐에 집어넣는다
for i in range(n):
    if arr1[i]==0:
        q.append(arr2[i])

for i in range(m):
    q.appendleft(arr3[i])
    print(q.pop(),end=" ")
