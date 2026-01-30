n,k=map(int,input().split())
arr=sorted(list(map(int,input().split())))
max_height=max(arr) #최대높이가 20이라면 0~20을 탐색할것임
#print("maxheight",max_height)

def wood_sum(arr,h):
    sum=0
    for a in arr:
        sum+=max(0,a-h)
    #print(f'자른 나무의 길이 합은 {sum}')
    return sum

# 처음 자른게 최적값일 수도 있음...
result=0
def bs(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2 # h값
        #print(f'h: {mid} 높이에서 자르겠습니다')
        if wood_sum(arr,mid)>=target: # h 높이에서 잘랐는데 목표보다 크거나 h~max에서 최적값 탐색(덜자르기)
            result=mid
            start=mid+1
        elif wood_sum(arr,mid)<target: # h 높이에서 잘랐는데 목표보다 부족하다면 0~h-1 에서 최적값 탐색(더자르기)
            end=mid-1 
    return result

print(bs(arr,k,0,max_height-1))
