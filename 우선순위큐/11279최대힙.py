import heapq
import sys
fast_input=sys.stdin.readline
heap=[]
n=int(input())

for i in range(n):
    val=int(fast_input())
    if val==0:
        if not heap:
            print(0)
            continue
        print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap,-val)
