"""
https://school.programmers.co.kr/learn/courses/30/lessons/42579

https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL3-%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%95%A8%EB%B2%94-Python

1.

"""
from collections import defaultdict

def solution(genres, plays):
    answer=[]
    dic={}
    popular=defaultdict(int) #인기 장르 카운트용
    # idx->(genre,play)로 해싱할것임
    for idx,(g,p) in enumerate(zip(genres,plays)):
        dic[idx]=(g,p)
        popular[g] += p

    #장르 순 정렬
    popular=sorted(popular,key=lambda x:popular[x],reverse=True)
    #장르 재생 횟수 순 정렬
    #인기 장르마다 각각 재생 횟수 순 정렬 후 answer 상위2개 append
    for g in popular:
        arr=[]
        for idx,v in dic.items():
            if v[0]==g:
                arr.append(idx)
        arr=sorted(arr,key=lambda x:dic[x][1],reverse=True)
        answer+=arr[:2]
    return answer

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

print(solution(genres, plays))