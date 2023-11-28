#입력 그래프의 인접 행렬 만들기
g = [[0,1,1,0,0,0,0,0,0,0],
     [1,0,1,1,1,0,0,0,0,0],
     [1,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,1,0,0,0],
     [0,1,0,1,0,0,0,0,0,0],
     [0,0,0,1,0,0,1,1,0,0],
     [0,0,0,1,0,1,0,1,0,0],
     [0,0,0,0,0,1,1,0,1,0],
     [0,0,0,0,0,0,0,1,0,1],
     [0,0,0,0,0,0,0,1,1,0]]
n = len(g)
K = 3
color = [-1 for i in range(n)]  #각 정점의 색을 -1로 초기화


#알고리즘 구현하기
def valid(i):
    for j in range(n):
        if g[i][j] and color[i] == color[j] and (color[i] != -1):
            return False
    return True

def coloring(i):
    if i== n:
        print('색칠결과:', color)
        return True

    for c in range(K):
        color[i]= c
        if valid(i):
            if coloring(i+1):
                return True
    return False

#실행해 보기

if not coloring(0):
    print('색칠 할 수 없음')
