#0초부터 n시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는 경우의 수
n=int(input())

count=0
for i in range(n,24):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in str(i) + str(j) + str(k):
                count +=1