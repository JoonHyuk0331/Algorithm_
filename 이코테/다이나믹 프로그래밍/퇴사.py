n=int(input())
mem=[0]*(n+1)

for day in range(1,n+1):
    duration,profit=map(int,input().split())
    if day+duration-1>n:
        continue
    mem[day+duration-1]=max(mem[day+duration-1],mem[day-1]+profit)
    mem[day] = max(mem[day], mem[day - 1])


#print(mem)
print(max(mem))
"""
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
"""