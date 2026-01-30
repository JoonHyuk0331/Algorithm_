"""
최대값을 찾아야함, 최대 힙 구현
순서 기억 후 원복 로직 잘 봐두기
line: 11,22,23
"""
import heapq
from heapq import heapify
import sys
input=sys.stdin.readline

N,K=map(int,input().split())
max_heap=[(-v,idx) for idx,v in enumerate(list(map(int,input().split())))]
#집어넣기
heapify(max_heap)

for i in range(K):
    if -max_heap[0][0]>100: #도둑질 할만하면
        v,index=heapq.heappop(max_heap)
        heapq.heappush(max_heap,(-((-v)-100),index))
    else:
        exit(print("impossible"))

ans1=sorted(max_heap,key=lambda x:x[1])
ans2=[-aa[0] for aa in ans1]
print(*ans2)