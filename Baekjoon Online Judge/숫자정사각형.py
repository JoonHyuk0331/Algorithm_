n,m=map(int,input().split())

board=[list(map(int,input())) for _ in range(n)]

min_len=min(n,m)
ans=0

for target in range(10): #0~9
    for i in range(n):
        for j in range(m):
            if board[i][j]==target:
                #print(f'검사시작:target={target},{i,j}')
                for k in range(m):
                    if j+k>=m or i+k>=n:
                        continue
                    #print(f'{i, j},{i, j + k},{i + k, j},{i + k, j + k}')
                    if board[i][j+k]==target and board[i+k][j]==target and board[i+k][j+k]==target:
                        ans=max(ans,(k+1)*(k+1))
                        #print(f'{k+1}x{k+1} 정사각형!')
print(ans)