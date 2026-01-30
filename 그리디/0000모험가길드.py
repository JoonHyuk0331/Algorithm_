n=int(input())
data=sorted(list(map(int,input().split())))

count=0
group=0
for i in data:
    count+=1
    if i<=count:
        group+=1
        count=0

print(group)
    
    

