from collections import deque

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1 , 0, 0]

# 테스트케이스 개수
t = int(input())

def bfs(x, y):
    queue = deque()
    queue.append((x, y))    # 해당 좌표 deque에 저장
    visited[x][y] = True     # 중복 방문 방지를 위해 방문 시 True 부여

    # 데큐에 제일 왼쪽에 있는 좌표를 꺼내 상하좌우 탐색
    # 배추가 있고, 방문하지 않은 곳이면 데큐에 저장하고 방문 처리
    while queue:
        x, y = queue.popleft()  
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] and not visited[nx][ny]:   
                queue.append((nx, ny))
                visited[nx][ny] = True

def dfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True     # 중복 방문 방지를 위해 방문 시 True 부여
    while queue:
        x, y = queue.pop()  

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] and not visited[nx][ny]:   
                queue.append((nx, ny))
                visited[nx][ny] = True

if __name__ == "__main__":
    for _ in range(t):
        m, n, k = map(int, input().split())
        board = [[0] * m for _ in range(n)]         # 배추밭 배열
        visited = [[False] * m for _ in range(n)]   # 방문 처리 배열
        # 배추 위치 받아오기
        for _ in range(k):
            x, y = map(int, input().split())
            board[y][x] = 1

        cnt = 0     # 지렁이 수
        # 배열 탐색하여 배추 존재하고, 방문하지 않았으면 BFS 실행 후 지렁이 수 증가
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1 and not visited[i][j]:
                    # dfs(i, j)
                    bfs(i, j)
                    cnt += 1
        print(cnt)