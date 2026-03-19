n=int(input())

for i in range(4500):
    if n-i>0:
        n-=i
    else:
        if i%2==0:
            print(f'{n}/{i+1-n}')
        else:
            print(f'{i+1-n}/{n}')
        break