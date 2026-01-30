# 대기 큐 [번호, 요청시각,소요시간]
#
# 우선순위 [1소요시간,2작업요청시각빠른것,3작업번호]
#
# 비선점
#
# 작업끝나면 대기 큐에서 다음 작업을 선택한다,
# 작업이 끝날때 대기 큐에 작업이 추가되면 이를 포함해서 평가한다
#
# 평균대기시간 반환
#
# 디스크 컨트롤러
#
# 새로운 작업 요청 확인해서 대기큐에 삽입
# 하드디스크 작업 진행, 작업이 끝났는지 확인
# 작업이 끝났다면 대기큐에 하드디스크에 작업 할당
#
# 대기큐의 설계
# 소요시간 순 최소 힙, 소요시간이 같은개 두개 나오면
#
#
# 둘다 꺼내서 2,3번 조건
# jobs[i]는 i번 작업에 대한 정보이고 [s, l] 형태입니다.
# s는 작업이 요청되는 시점이며 0 ≤ s ≤ 1,000입니다.
# l은 작업의 소요시간이며 1 ≤ l ≤ 1,000입니다.

import heapq

def solution(jobs):
    heap=[]
    time_mem=[0]*501
    #jobs에 순번 추가
    for idx,job in enumerate(jobs):
        jobs[idx].append(idx)
        #print(jobs)
    job_cnt=len(jobs)
    hd=[]
    time=0
    while True:
        #print(f'st===={time}')
        # jobs에서 해당 시간대에 새로운 작업 요청이 있는지 확인
        for job in jobs:
            if job[0]==time:
                heapq.heappush(heap, [job[1],job[0],job[2]]) #있다면 대기큐에 삽입
                job_cnt-=1

        if hd: #하드에 뭔가 있다면
            #print(f'하드디스크 작업 진행 {hd}')
            hd[0][0]-=1 #작업진행
            #print(f'하드디스크 작업 완료 {hd}')
            if hd[0][0]<=0:
                #print(f'하드디스크 작업 종료!!! {hd}')
                time_mem[hd[0][2]]=time-hd[0][1]
                #print(f'{time_mem[hd[0][2]]}={time}-{hd[0][1]}')
                hd.pop()
                if not heap and job_cnt<=0:
                    #print("모든작업이종료되었습니다")
                    break
                if heap:
                    hd.append(heapq.heappop(heap)) #새로운 작업 할당
        else:
            if heap:
                job=heapq.heappop(heap)
                #print(f'새로운작업할당{job}')
                hd.append(job) # 소요시간,요청시점,고유번호

        #print(f'ed===={time}')
        time += 1

    answer = 0
    sum=0
    for i in range(len(time_mem)):
        sum+=time_mem[i]
    #print(sum//len(jobs))

    return sum//len(jobs)

print(solution([[0, 3], [1, 9], [2, 6], [30, 3]])) #작업번호 0 index이므로 주의 요청되는시간,소요시간