from collections import defaultdict


def solution(edges):
    edge_cnt = defaultdict(lambda :[0,0]) # out,in
    ans=[0,0,0,0] # 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수

    for a, b in edges:
        edge_cnt[a][0]+=1 #a나가는 간선 추가
        edge_cnt[b][1]+=1 #b들어오는 간선 추가

    for key,val in edge_cnt:
        if val[1]==1:
            ans[2]+=1
        elif val[1]>=2 and val[0]>=2:
            ans[3]+=1
        elif val[1]==0 and val[0]>=2:
            ans[0]=key
    ans[1]=(edge_cnt[ans[0]][0]-ans[2]-ans[3])

    return ans


    #in 1: 막대
    #in over2 out 2: 8자
    #in 0 out 2over: 생성된정점
    #생성된정점-막대-8자=도넛모양그래프 개수



