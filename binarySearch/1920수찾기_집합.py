n=int(input())
set=set(map(int,input().split()))
m=int(input())
target_list=list(map(int,input().split()))

for target in target_list:
    if target in set:
        print(1)
    else:
        print(0)