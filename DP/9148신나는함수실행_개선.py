dp=[[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    #핵심 코드 w(a,b,c) 값이 이미 있다면 리턴한다
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        # a<b<c인 경우 dp값 갱신
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    #dp값 갱신
    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]

while True:
    aa,bb,cc=map(int,input().split())
    if aa==-1 and bb==-1 and cc==-1:
        break
    print(f'w({aa}, {bb}, {cc}) = {w(aa,bb,cc)}')


