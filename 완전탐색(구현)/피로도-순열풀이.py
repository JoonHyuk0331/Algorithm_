from itertools import permutations

def solution(k, dungeons):
    answer = -1
    cases=list(permutations(dungeons,len(dungeons)))
    #[([80, 20], [50, 40], [30, 10]), ([80, 20], [30, 10], [50, 40]),....]
    for case in cases: #각각의 경로마다
        cnt=0
        fatigue=k
        for dungeon in case: #각각의 경로마다
            if dungeon[0]<=fatigue:
                cnt+=1
                fatigue=fatigue-dungeon[1]
            else:
                break
        answer=max(answer,cnt)

    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))