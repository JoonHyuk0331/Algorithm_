import copy

# 1. 방향 정의 (0~7 인덱스)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 입력받을 때 방향에서 1을 미리 빼서 0~7로 맞춤
matrix = [[] for _ in range(4)]
for r in range(4):
    row = list(map(int, input().split()))
    for idx in range(0, 8, 2):
        matrix[r].append([row[idx], row[idx + 1] - 1])  # 방향에 -1

max_cnt = 0


def move_fish(now_matrix, sx, sy):
    for f_num in range(1, 17):
        pos = None
        for x in range(4):
            for y in range(4):
                if now_matrix[x][y][0] == f_num:
                    pos = (x, y)
                    break
            if pos: break

        if not pos: continue
        x, y = pos
        f_n, f_d = now_matrix[x][y]

        for i in range(8):
            nd = (f_d + i) % 8  # 이제 f_d가 0~7이므로 그냥 i만 더하면 됨
            nx, ny = x + dx[nd], y + dy[nd]

            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == sx and ny == sy):  # 상어가 없는 칸으로만
                    now_matrix[x][y][1] = nd  # 바뀐 방향 저장
                    now_matrix[x][y], now_matrix[nx][ny] = now_matrix[nx][ny], now_matrix[x][y]
                    break
    return now_matrix


def dfs(sx, sy, score, current_matrix):
    global max_cnt
    # 원본 보존을 위한 copy
    board = copy.deepcopy(current_matrix)

    # 1. 상어가 물고기를 먹음
    fish_num, fish_dir = board[sx][sy]
    score += fish_num
    max_cnt = max(max_cnt, score)
    board[sx][sy] = [0, -1]  # 물고기 사라짐 (번호 0)

    # 2. 물고기 이동 (상어 위치 sx, sy 전달)
    move_fish(board, sx, sy)

    # 3. 상어 이동 시도 (먹은 물고기의 방향 fish_dir로 이동)
    for step in range(1, 4):
        nx, ny = sx + dx[fish_dir] * step
        ny = sy + dy[fish_dir] * step

        if 0 <= nx < 4 and 0 <= ny < 4:
            if board[nx][ny][0] > 0:  # 물고기가 있는 칸으로만 이동 가능
                dfs(nx, ny, score, board)


# 시작: (0,0) 위치에서 먹고 시작
dfs(0, 0, 0, matrix)
print(max_cnt)