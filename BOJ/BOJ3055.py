from collections import deque;

# 위 아래 왼쪽 오른쪽 방향 벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]



def Bfs():
    minute = 0
    while hedgehog:
        minute += 1
        # 물일 때
        for _ in range(len(water)):
            x, y = water.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < c and 0 <= ny < r:
                    if board[nx][ny] == '.'  and not visited[nx][ny]:
                        board[nx][ny] = '*'
                        water.append((nx, ny))

        # 고슴이일 때
        for _ in range(len(hedgehog)):
            x, y = hedgehog.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < c and 0 <= ny < r:
                    if board[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        hedgehog.append((nx, ny))
                    if board[nx][ny] == 'D' :
                        return print(minute)
    
    return print("KAKTUS")
                

if __name__ == "__main__":
    c, r = map(int, input().split())
    board = [list(map(str, input().strip())) for _ in range(c)]
    visited = [[False] * r for _ in range(c)]
    hedgehog = deque()
    water = deque()

    for i in range(c):
        for j in range(r):
            if board[i][j] == '*':
                water.append((i, j))
            elif board[i][j] == 'S' and not visited[i][j]:
                hedgehog.append((i, j))
                visited[i][j] = True

    Bfs()

# 고슴도치: S
# 비버 굴: D
# 물: *
# 돌: X