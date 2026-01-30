#1822 이분탐색 set 자료형이 아닌 이분탐색으로 풀이
#remove 사용 시 시간초과

n1,n2=map(int,input().split())
arrA=sorted(list(map(int,input().split())))
arrB=list(map(int,input().split()))

def bs(target,arr): # binarySearch 돌려서 있으면 False 없으면 True 뱉음
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return False
        if arr[mid]>target: # target.. mid
            end=mid-1
        else:
            start=mid+1
    return True

# for i in arrB:
#     if bs(i,arrA):
#         arrA.remove(i) <- 시간초과 냄

res=[]

for i in arrA:
    if bs(i,arrB): # arrA가 arrB에 들어있지 않다면(True)
        res.append(i)

print(len(res))
print(' '.join(map(str,res)))