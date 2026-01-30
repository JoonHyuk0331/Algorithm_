"""
백트래킹 풀이
"""

import sys
sys.setrecursionlimit(10**6)

def solution(k, dungeons):
    answer = -1
    def dfs(fat,vis,depth):
        nonlocal answer
        answer=max(depth,answer)
        for idx,dungeon in enumerate(dungeons):
            if dungeon[0]<=fat and not vis[idx]:
                vis[idx]=1
                dfs(fat-dungeon[1],vis,depth+1)
                vis[idx]=0

    v=[0]*(len(dungeons)+1)
    dfs(k,v,0)

    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))