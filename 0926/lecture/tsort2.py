from collections import deque

adj_list = [[1], [4, 3], [1, 0],
            [6], [5], [7, 3], [7], [8], []]
n = len(adj_list)
in_degree = [1,2,0,2,1,1,1,2,1]


def tsort():
    result = []         #위상정렬 결과를 저장할 리스트
    queue = deque() 

    #진입차수가 가장 적은 정점을 찾아 큐에 넣는다.
    for i in range(0, n):
        if in_degree[i] == 0:
            queue.append(i)
    
    #큐에서 정점을 하나 꺼낸다. 걔가 now!
    while queue:
        #정점하나 방문하기!
        now = queue.popleft()
        result.append(now) 

        #현재 방문한 정점의 인접 리스트에 있는 각 정점의 진입차수를 1낮춘다.
        for i in adj_list[now]:
            in_degree[i] -= 1
            #낮추면서 진입차수가 0이되는 곳은 방문해야 하니 큐에 넣는다.
            if in_degree[i] == 0:
                queue.append(i)
        #이렇게 방문한 정점의 인접한 정점의 진입차수를 수정하며 
        #큐에 추가하는 작업이 끝나면
        #while의 다음 반복으로 넘어가서 다음 점을 방문하게 된다.
    
    print(result)

tsort()