n=int(input())
numbers=list(map(int,input().split()))
m=int(input())
finds=list(map(int,input().split()))
numbers.sort()
# x->target이 위치한 인덱스
def bs(st,en,target,arr):
    while st<=en:
        mid = (st + en) // 2
        if arr[mid]==target:
            return True #0으로하면 False떠서 그럼
        elif arr[mid]<target:
            st=mid+1
        else:
            en=mid-1
    return False

for f in finds:
    if bs(0,n-1,f,numbers):
        print(1)
    else:
        print(0)
