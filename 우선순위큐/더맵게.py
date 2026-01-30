import heapq

def solution(scoville, K):

    cnt=0
    heap=[]
    for val in scoville:
        heapq.heappush(heap,val)

    while True:
        if heap[0]>=K:
            break

        if len(heap)<2:
            return -1

        a=heapq.heappop(heap)
        b=heapq.heappop(heap)
        heapq.heappush(heap,a+b*2)
        cnt+=1

    return cnt

print(solution([1, 2, 3, 9, 10, 12],7))