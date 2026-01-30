n=int(input())
list=[int(input()) for _ in range(n)]
list.sort()

len=n
w=0
for i in range(n):
    #print(f'list[{i}]: {list[i]}, len: {len} w: {w}')
    w=max(w,list[i]*len)
    len-=1

print(w)
    