n, K = map(int, input().split())
W=[]*n
V=[]*n

for i in range(n-1):
    W[i], V[i] = map(int,input().split())

T = [[0 for _ in range(K+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(K+1):
        if W[i] > j:
            T[i][j] = T[i-1][j]
        else:    
            T[i][j] = max(T[i-1][j], V[i]+T[i-1][j-W[i]])

print(T[n-1][K])       

