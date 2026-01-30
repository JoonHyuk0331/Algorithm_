m,n=map(int,input().split()) #나눠줘야하는 개수,전체과자개수
arr=sorted(list(map(int,input().split())))

#parametrix search 유형
#0~10범위에서 탐색해서 작은것부터 점점 크게 잘라서 안될때까지 찾는다

def ps(arr):
    start=1
    end=max(arr)
    while(start<=end):
        mid=(start+end)//2
        splitAbleCount=0#나눠줄수있는 막대과자 개수
        for i in arr:
            if i//mid:#1이상으로 나뉘어지면
                splitAbleCount+=i//mid

        if splitAbleCount>=m:#나눠줄수 있다면 더 큰 값에서 탐색해야함
            start=mid+1
        else:
            end=mid-1
    return end        
        
print(ps(arr))