import sys
import heapq
input=sys.stdin.readline

n=int(input())

arr=[]
total=0

for i in range(n):
    arr.append(int(input()))

heapq.heapify(arr)

for j in range(n-1):

    a=heapq.heappop(arr)
    b=heapq.heappop(arr)
    total+=(a+b)
    heapq.heappush(arr,a+b)

print(total)