import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().strip().split()))
m=int(input())
targetList=list(map(int,input().strip().split()))
result=[0]*m

def bs(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid+1
        if arr[mid]<=target:
            start=mid+1
        else:
            end=mid-1

def low_idx(arr,target,len):
    st=0
    en=len
    while st<en:
        mid=(st+en)//2
        if arr[mid]>=target:
            en=mid
        else:
            st=mid+1
    return st

def up_idx(arr,target,len):
    st=0
    en=len
    while st<en:
        mid=(st+en)//2
        if arr[mid]>target:
            en=mid
        else:
            st=mid+1
    return st #mid로 하면 안된다
            
#arr을 정렬한다
arr.sort()
#arr에서 이분탐색해서 n번째에 있으면 result값을 증가시킨다
for i in range(m):
    result=up_idx(arr,targetList[i],n)-low_idx(arr,targetList[i],n)
    print(result,end=" ")
