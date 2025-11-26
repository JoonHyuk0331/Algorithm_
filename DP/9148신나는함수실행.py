# w(a,b,c)의 결과를 어디에 적어두면 좋지 않을까 탑다운으로 풀어보자

"""
현재 풀이에선 w(a,b,c)의 가지들인 w(a,b,c-1),w( ~~~~) 를 다 계산했지만
결국 w(a,b,c)의 결과만 알면 되므로 하나씩 다 할 필요 없다
개선 풀이 방법 참고
"""
dp=[[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if a < b < c:
        if dp[a][b][c-1]==0:
            dp[a][b][c-1]=w(a,b,c-1)
        s1=dp[a][b][c-1]

        if dp[a][b-1][c-1]==0:
            dp[a][b - 1][c - 1]=w(a, b-1, c-1)
        s2=dp[a][b-1][c-1]

        if dp[a][b-1][c]==0:
            dp[a][b - 1][c]=w(a, b-1, c)
        s3=dp[a][b-1][c]

        return s1+s2-s3

    if dp[a-1][b][c]==0:
        dp[a - 1][b][c]=w(a-1, b, c)
    s1=dp[a - 1][b][c]

    if dp[a-1][b-1][c]==0:
        dp[a-1][b-1][c]=w(a-1,b-1,c)
    s2=dp[a-1][b-1][c]

    if dp[a-1][b][c-1]==0:
        dp[a-1][b][c-1]=w(a-1,b,c-1)
    s3=dp[a-1][b][c-1]

    if dp[a-1][b-1][c-1]==0:
        dp[a-1][b-1][c-1]=w(a-1,b-1,c-1)
    s4=dp[a-1][b-1][c-1]

    return s1+s2+s3-s4

while True:
    aa,bb,cc=map(int,input().split())
    if aa==-1 and bb==-1 and cc==-1:
        break
    print(f'w({aa}, {bb}, {cc}) = {w(aa,bb,cc)}')


