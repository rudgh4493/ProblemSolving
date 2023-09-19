adj_list=[[1,2],[0,3],[0,4],[1,4],[2,3]]
n=len(adj_list)
visited=[False for _ in range(n+1)]
        
def dfs(v):
    visited[v]=True
    print(v,'',end='')
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)

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

print('DFS 방문 순서:')
for i in range(n):
    if not visited[i]:
        dfs(i)
print("\n")

visited=[False for _ in range(n+1)]

print('BFS 방문 순서:')
for i in range(n):
    if not visited[i]:
        bfs(i)