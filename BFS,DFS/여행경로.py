"""
경로 복원
"""

from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)  # dict에 없는 key 값으로 value가 빈 list로 초기화되어 저장
    for ticket in tickets:
        key, val = ticket
        graph[key].append(val)

    for key in graph:
        graph[key].sort(reverse=True)  # 리스트 cba순 정렬

    def dfs(v):
        # 해당 v에서 할 수 있는 액션
        while graph[v]:  # graph[v] 에서 할 수 있는 액션이 남아 있는 동안
            next_v = graph[v].pop()
            dfs(next_v)

    answer = []
    return answer