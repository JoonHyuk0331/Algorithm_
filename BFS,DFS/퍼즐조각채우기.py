from collections import deque

def solution(game_board, table):
    vis_table = [[0] * 51 for _ in range(51)]
    vis_board = [[0] * 51 for _ in range(51)]
    key_size = 0

    # 디버깅용 그래프 출력
    def printg(g):
        n = len(g)
        m = len(g[0])
        for i in range(n):
            for j in range(m):
                print(g[i][j], end='')
            print()

    # 90도 회전
    def rotate90(matrix):
        n = len(matrix)
        m = len(matrix[0])
        rotated = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                rotated[j][n - 1 - i] = matrix[i][j]
        return rotated

    # 조각을 감싸는 직사각형 형태로 정규화 0 기준
    def normalize_board(graph):
        n, m = len(graph), len(graph[0])
        x = []
        y = []
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    x.append(i)
                    y.append(j)
        r = max(x) - min(x) + 1
        c = max(y) - min(y) + 1
        nom_graph = [[0] * c for _ in range(r)]
        for i in range(n):
            for j in range(m):
                if not graph[i][j]:
                    nom_graph[i - min(x)][j - min(y)] = 1
        return nom_graph

    # 조각을 감싸는 직사각형 형태로 정규화 1 기준
    def normalize_table(graph):
        n, m = len(graph), len(graph[0])
        x = []
        y = []
        for i in range(n):
            for j in range(m):
                if graph[i][j]:
                    x.append(i)
                    y.append(j)
        r = max(x) - min(x) + 1
        c = max(y) - min(y) + 1
        nom_graph = [[0] * c for _ in range(r)]
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    nom_graph[i - min(x)][j - min(y)] = 1
        return nom_graph

    # 패턴 찾아서 정규화해서 넣기
    def bfs_board(x, y, board):
        return_board = [[0] * 51 for _ in range(51)]
        n, m = len(board), len(board[0])
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        q = deque([(x, y)])
        vis_board[x][y] = 1
        return_board[x][y] = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 0 and not vis_board[nx][ny]:
                        q.append((nx, ny))
                        vis_board[nx][ny] = 1
                        return_board[nx][ny] = 1
        return return_board

    # 패턴 찾아서 정규화해서 넣기
    def bfs_table(x, y, graph):
        nonlocal key_size
        return_board = [[0] * 51 for _ in range(51)]
        n, m = len(graph), len(graph[0])
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        q = deque([(x, y)])
        vis_table[x][y] = 1
        return_board[x][y] = 1
        key_size += 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 and not vis_table[nx][ny]:
                        q.append((nx, ny))
                        vis_table[nx][ny] = 1
                        return_board[nx][ny] = 1
                        key_size += 1
        return return_board
    cnt=0
    pattern_list = []
    key_list=[]

    for k in range(len(game_board)):
        for l in range(len(game_board[0])):
            # bfs 돌려서 나온 vis 를 정규화해서 집어넣는다
            if not vis_board[k][l] and game_board[k][l]==0:
                pattern_list.append(normalize_table(bfs_board(k,l,game_board)))

    for k in range(len(table)):
        for l in range(len(table[0])):
            # bfs 돌려서 나온 vis 를 정규화해서 집어넣는다
            if not vis_table[k][l] and table[k][l]==1:
                key_list.append(normalize_table(bfs_table(k,l,table)))

    for pattern in pattern_list: #각 패턴마다
        #print("++++NEW PATTERN++++")
        #printg(pattern)
        flag=0
        for idx,key in enumerate(key_list):
            if not flag:
                for _ in range(4):
                    #print("===============")
                    key=rotate90(key)
                    #print("now_key---")
                    #printg(key)
                    #print("pattern---")
                    #printg(pattern)
                    if key==pattern:
                        #print("O")
                        cnt+=1
                        del key_list[idx]
                        flag=1
                        break
                    # else:
                    #     #print("X")

    left_cnt=0
    for key in key_list:
        #print("left key~~~~~~")
        #printg(key)
        for o in range(len(key)):
            for p in range(len(key[0])):
                if key[o][p]==1:
                    left_cnt+=1
    return key_size-left_cnt
# printg(normalize_table((bfs_board(0,2,[[1,1,0,1],
#                        [1,0,0,1],
#                        [1,1,1,1]]
#                        ))))
# printg(normalize_table((bfs_table(0,2,[[0,0,1,0],
#                        [0,1,1,0],
#                        [0,0,0,0]]
#                        ))))
#print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
print(solution([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]]))