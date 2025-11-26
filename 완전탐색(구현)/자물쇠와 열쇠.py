from copy import deepcopy
def rotate90(matrix):
    size = len(matrix)
    rotated_matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            rotated_matrix[j][size - i - 1] = matrix[i][j]
    return rotated_matrix


def larger_matrix(matrix, up_scale):
    # 테두리 up_scale 생김
    matrix_size_origin = len(matrix)
    scaled_size = matrix_size_origin + (2 * up_scale)
    large_matrix = [[0] * scaled_size for _ in range(scaled_size)]
    for i in range(matrix_size_origin):
        for j in range(matrix_size_origin):
            large_matrix[i + up_scale][j + up_scale] = matrix[i][j]
    return large_matrix


def solution(key, lock):
    m = len(key)
    n = len(lock)
    # 필수 요소 추출
    graph = larger_matrix(lock, m)
    graph_size = len(graph)

    for _ in range(4):
        
        for i in range(graph_size - m):
            for j in range(graph_size - m):
                
                temp_graph = deepcopy(graph)
                for a in range(m):
                    for b in range(m):
                        temp_graph[i + a][j + b] += key[a][b]
                flag = True
                for a in range(n):
                    for b in range(n):
                        if temp_graph[m + a][m + b] != 1:
                            flag = False
                if flag:
                    return True
                
        key = rotate90(key)
        
    return False