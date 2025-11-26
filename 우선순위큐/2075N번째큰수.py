"""
메모리 제한도 확인해야하는 문제
1500x1500x(파이썬int:28byte) = 63,000,000 바이트 = 63000mb
-> 통째로 트리등의 자료구조에 박으면 메모리초과

시간복잡도 고려
일반 배열에 넣을 경우 삽입O(n) 후 오름차순 전체정렬O(n),O(nlogn)
이 걸리므로 시간초과
힙에 넣으면 삽입시 O(n) 밖에 안걸리므로 괜찮음
->heap 사용
"""

"""
최소힙 사용
사용할 힙 heap은 n개 배열로 할당되며
일종의 왕좌? 라고 생각하면됨

새로 힙에 넣을 숫자와 최소힙 루트를 비교해 최소힙 루트보다 작으면 넣지 말고 패스
루트보다 크면 pop하고 새로 넣기 

n번째 큰 수 = 요소의 개수가 n인 최소 힙의 루트
"""

import heapq

heap=[]

n=int(input())

data=list(map(int,input().split()))
for j in data:
    heapq.heappush(heap,j)

for i in range(1,n):
    data=map(int,input().split())
    for j in data:
        if j>heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,j)


print(heap[0])