n=int(input())
arr=list(map(int,input().split()))
arr_set=sorted(list(set(arr)))

def bs(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        #print(f'arr의 크기는{len(arr)} mid의 크기는{mid}')
        if arr[mid]==target:
            return mid
        if arr[mid]>target:
            end=mid-1
        else:
            start=mid+1

for i in range(n):
    print(bs(arr_set,arr[i],0,len(arr_set)-1),end=" ")