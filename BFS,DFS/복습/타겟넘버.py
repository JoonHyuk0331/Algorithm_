from collections import deque
import sys

sys.setrecursionlimit(100000)


def solution(numbers, target):
    cnt=0
    stk=[(0,0)] # idx,total
    while stk:
        idx,total=stk.pop()
        if idx==len(numbers):
            if total==target:
                cnt+=1
            continue
        stk.append((idx+1,total+numbers[idx]))
        stk.append((idx+1,total-numbers[idx]))
    return cnt