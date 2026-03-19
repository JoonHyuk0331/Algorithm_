import sys

input=sys.stdin.readline
n,e=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
size=len(nums)
cnt=0
for i in range(size-1):
    if nums[i+1]-nums[i]>=e:
        cnt+=1
print(cnt+1)