#덱에 넣기
#<나오면 지금까지 나온건 다 pop로 출력하고 >나올때까지 계속 입력받다가 다 popleft로 빼면서 출력
#공백나오면 지금까지 다 pop로 뺴면서 출력

from collections import deque
s=input()
q=deque()
tag_on=0 # tag_on=1:>를 기다리며 다 입력받는 상태
for c in s:
    if tag_on:
        q.append(c)
        if c=='>':
            tag_on=0
            while q:
                print(q.popleft(), end="")
    elif c=='<':
        tag_on=1
        while q:
            print(q.pop(),end="")
        print("<", end="")
    elif c==' ':
        while q:
            print(q.pop(),end="")
        print(" ",end="")
    else:
        q.append(c)
if q:
    while q:
        print(q.pop(), end="")