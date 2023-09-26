
adj_list=[[1],[3,4],[0,1],[6],[5],[3],[7],[8],[]]
n=len(adj_list)
visited=[False for _ in range(n+1)]
s=[]

def dfs(v):
    visited[v]=True
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)
    s.append(v)  
    

for i in range(n):
    if not visited[i]:
        dfs(i)
s.reverse() #s를 역순으로함
print('위상 정렬 순서:',s)