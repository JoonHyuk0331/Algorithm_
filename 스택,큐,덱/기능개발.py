def solution(progresses, speeds):
    answer = []
    stk = []
    for i in range(len(progresses) - 1, -1, -1):
        stk.append([progresses[i], speeds[i]])

    while stk:
        cnt = 0
        for j in range(len(stk)):
            stk[j][0] += stk[j][1]
        while True:
            if stk and stk[-1][0] >= 100:
                stk.pop()
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)

    return answer