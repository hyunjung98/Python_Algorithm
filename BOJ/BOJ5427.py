from collections import deque;

# 동서남북 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 테스트 케이스 개수
t = int(input())

def Bfs():
    time = 0
    while person:
        time += 1
        for _ in range(len(fire)):
            x, y = fire.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] == '.' and not visited[nx][ny]:
                        board[nx][ny] = '*'
                        fire.append((nx, ny))
        for _ in range(len(person)):
            x, y = person.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] == '.' and not visited[nx][ny]: 
                        visited[nx][ny] = True
                        person.append((nx, ny))
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return print(time)
                    
    return print("IMPOSSIBLE")

if __name__ == "__main__":
    for _ in range(t):
        w, h = map(int, input().split())
        board = [list(map(str, input().strip())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        
        person = deque()
        fire = deque()

        for i in range(h):
            for j in range(w):
                if board[i][j] == '*':
                    fire.append((i, j))
                elif board[i][j] == '@':
                    person.append((i, j))
                    visited[i][j] = True
        Bfs()