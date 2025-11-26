#deque엔 rotate 함수가 있다
#[ a b c ] -> [ c a b ] appendleft(q.pop())과 동일

#enumerate()는 파이썬 내장 함수로, 리스트나 iterable 객체를 순회할 때 인덱스(순번)와 값을 함께 반환
#arr=[[val,idx]for idx,val in enumerate(arr,start=1)]

from collections import deque

n=int(input())
arr=list(map(int,input().split()))

d=deque()

idx=1
for i in arr:
    d.append([i,idx])
    idx+=1

def rotate_deque(num):
    if num>0:
        d.rotate(-(num-1))
    else:
        d.rotate(-num)


for i in range(n):
    #print(f'{i+1}회전: {d}')
    data=d.popleft()
    rotate_deque(data[0])
    print(data[1],end=" ")
    #print(f'{i + 1}회전종료: {d}')

