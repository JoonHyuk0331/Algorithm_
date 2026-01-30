from collections import deque

N,L=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.insert(0,0)
q=deque()

for i in range(1,N+1):
    if q:
        if i-L>=1 and q[0]==numbers[i-L]:
            q.popleft()
        while q and q[-1]>numbers[i]:
            q.pop()
    q.append(numbers[i])
    print(q[0],end=" ")