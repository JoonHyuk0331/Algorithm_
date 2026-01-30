from collections import defaultdict

def solution(word):

    ans=0
    cnt=0 #dfs실행횟수
    vis=defaultdict(int) #기본값 0
    alpha=['A', 'E', 'I', 'O', 'U']

    def dfs(string):
        nonlocal cnt
        nonlocal ans
        vis[string]=1 #방문처리
        cnt+=1
        #print(f'{cnt}:{string}')
        if string==word:
            ans=cnt
            return
        for a in alpha:
            nx_string=string+a
            if len(nx_string)>5:
                continue
            if not vis[nx_string]: #방문하지 않았다면
                vis[nx_string]=1
                dfs(nx_string)
    for b in alpha:
        dfs(b)

    return ans

print(solution('AO'))