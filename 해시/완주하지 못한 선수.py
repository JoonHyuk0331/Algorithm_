"""
https://school.programmers.co.kr/learn/courses/30/lessons/42576
"""

#시간초과 풀이
def solution1(participant, completion):

    for item in completion:#completion순회 O(n)
        participant.remove(item) #remove는 느려요! O(n)

    return participant

#카운터 풀이
from collections import Counter
def solution2(participant, completion):

    cnt=Counter(participant)-Counter(completion)

    return list(cnt.keys())[0]

participant=["leo", "kiki", "eden"]
completion=	["eden", "kiki"]
print(solution1(participant, completion))