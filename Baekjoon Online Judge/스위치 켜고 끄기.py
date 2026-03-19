switches_cnt=int(input())
switches=list(map(int,input().split()))
t=int(input())

# n을 입력받으면 n*1-1 n*2-1 n*3-1 스위치 토글
def man(n):
    target=0
    idx=0
    while target<switches_cnt-1:
        idx+=1
        target=n*idx-1
        if target >= switches_cnt :
            break
        #print(target)
        if switches[target]:
            switches[target] = 0
        else:
            switches[target] = 1

# n을 입력받으면 n-1 주위의 n-2 n 쌍 같은지 검사 후 바꾸기
def woman(n):
    same_cnt=0
    st=n-2
    en=n
    while 0<=st<switches_cnt and 0<=en<switches_cnt:
        if switches[st]==switches[en]:
            same_cnt+=1
        else:
            break
        st-=1
        en+=1
    for i in range(1,same_cnt+1):
        if switches[n-1-i]:
            switches[n-1-i] = 0
        else:
            switches[n-1-i] = 1
        if switches[n-1+i]:
            switches[n-1+i] = 0
        else:
            switches[n-1+i] = 1
    if switches[n - 1]:
        switches[n - 1] = 0
    else:
        switches[n - 1] = 1

for _ in range(t):
    s,nn=map(int,input().split())

    if s==1:
        man(nn)
    else:
        woman(nn)
for kkk in range(len(switches)):
    print(switches[kkk], end=' ')
    if (kkk+1)%20==0:
        print()
