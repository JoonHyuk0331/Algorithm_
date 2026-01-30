# 데이터의 개수가 1000만개를 넘어가거나 탐색 범위의 크기가 1000억 이상이라면 이진 탐색 고려
n=int(input())
ls=list(map(int,input().split()))
m=int(input())
target_list=list(map(int,input().split()))
ls.sort()

def bs(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid+1
        if arr[mid]<=target:
            start=mid+1
        else:
            end=mid-1


for i in range(m):
    #for target in target_list로 개선
    target=target_list[i]
    #print(f'find target:{target}')
    if bs(ls,target,0,n-1):
        print(1)
    else:
        print(0)