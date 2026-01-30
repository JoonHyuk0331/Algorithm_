from collections import deque
def solution(n, wires):
    first_cnt=0
    def bfs(graph,v):
        cnt=1
        q=deque([v])
        vis[v]=1
        while q:
            cur=q.pop()
            for g in graph[cur]:
                if not vis[g]:
                    q.append(g)
                    vis[g]=1
                    cnt+=1

        return cnt

    ans=999
    for i in range(1,len(wires)+1):# i를 빼고 진행하기
        vis = [0] * (n + 1)
        board = [[] for _ in range(n + 1)]
        for idx,wire in enumerate(wires):
            if idx+1==i:
                continue
            v1 = wire[0]
            v2 = wire[1]
            board[v1].append(v2)
            board[v2].append(v1)
        for j in range(1,n+1):
            if not vis[j]:
                first_cnt=(bfs(board,j))
                break
        other_cnt=n-first_cnt
        ans=min(ans,abs(first_cnt-other_cnt))
    return ans

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))