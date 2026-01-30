n=int(input())

listA=sorted(list(map(int,input().split())))
listB=sorted(list(map(int,input().split())),reverse=True)

#print(listA)
#print(listB)

ans=0
for i in range(n):
    ans+=listA[i]*listB[i]
print(ans)