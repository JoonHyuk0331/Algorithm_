import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
targetList=list(map(int,input().split()))
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
            

#arr을 정렬한다
arr.sort()
#arr에서 이분탐색해서 n번째에 있으면 result값을 증가시킨다
for i in range(m):
    while bs(arr,targetList[i],0,len(arr)-1):#매번 bs마다 O(n)연산인 len()를 실행하는 문제
        result[i]+=1
        arr.remove(targetList[i])#remove연산도 O(n) 임

#result를 출력한다
print(' '.join(map(str,result)))