def printGraph(graph, n, m,title):
    print(f'==={title}===')
    for i in range(n):
        for j in range(m):
            print(f"{graph[i][j]:3}", end=" ")
        print()
    print()