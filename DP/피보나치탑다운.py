#메모리제이션 기법을 이용한 피보나치 수열 구하기
#큰 문제를 해결하기 위해 작은 문제를 호출하는 방식
d=[0]*100

def fibo(x):
    if x==1 or x==2: # 종료조건
        return 1
    if d[x]!=0: #이미 계산 한 적 있다면
        return d[x] # 계산했던거 리턴한다
    d[x]=fibo(x-1)+fibo(x-2) #피보나치 계산
    return d[x]

print(fibo(99))