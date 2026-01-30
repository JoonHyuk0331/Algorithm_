# a+b+c=k
# a+b=k-cx
# 이렇게 뭔가 2개의 값을 묶은 후 어느 한쪽의 값을 이분탐색으로 찾아서 시간복잡도를 낮추는 아이디어

def bs(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid+1
        if arr[mid]<=target:
            start=mid+1
        else:
            end=mid-1

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort()
sums=[]
for i in range(n):
    for j in range(n): #x,y,z 가 서로 같아도 됨
        a=arr[i]
        b=arr[j]
        sums.append(a+b)

sum_set=set(sums)
sums=sorted(list(sum_set)) #중복 제거후 정렬

#print("가능한 sums 경우의 수 리스트는:",end='')
#print(sums)

max_k=0
for i in range(n):
    for j in range(n):
        c=arr[i]
        k=arr[j]
        target=k-c
        if target>0: #음수는 할 필요 없음
            #print(f'c:{c} k:{k} 에 대해 {target}이 sums에 있는지 이분탐색합니다')
            if bs(sums,target,0,len(sums)-1): # 있는 경우의 수라면
                #print(f'c:{c} k:{k} 에 대해 {target}이 sums에 존재합니다')
                max_k=max(max_k,k) #c 값을 최대로 갱신

print(max_k) #값 출력