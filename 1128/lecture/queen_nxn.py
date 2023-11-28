#입력 값 처리 및 보드 초기화
print('여왕 말의 수 : ', end='')
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)] #nxn 보드초기화'

#알고리즘 구현하기

def is_threatening(i,j):
    for k in range(n):
        if board[i][k] == 1 or board[k][j] ==1:
            return True
        
    for k in range(n):
        for l in range(n):
            if(k+l == i+j) or (k-l ==i-j):
                if board[k][l]==1:
                    return True
    return False

def queen(i):
    if i == n:
        return True
    for j in range(n):
        if(not(is_threatening(i, j)))and (board[i][j] != 1):
            board[i][j] = 1
            if queen(i+1):
                return True
            board[i][j] = 0
    return False

#실행해 보기

queen(0)
for x in board:
    print(*x, sep=" ")