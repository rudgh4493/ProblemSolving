adj_list=[[2,1],[3,0],[3,0],[9,8,2,1],[5],[7,6,4],[7,5],[6,5],[3],[3]]
n=len(adj_list)
visited=[False for _ in range(n+1)]

def bfs(v):
    queue=[]
    visited[v]=True
    queue.append(v)
    while len(queue)!=0:
        u=queue.pop(0)
        print(u, '', end='')
        for w in adj_list[u]:
            if not visited[w]:
                visited[w]=True
                queue.append(w)

print('BFS 방문 순서:')
for i in range(n):
    if not visited[i]:
        bfs(i)