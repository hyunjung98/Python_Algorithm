from collections import deque;

# 상하좌우 방향벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0

def Bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 현재 값과 상하좌우 값 비교하여 같으면 큐에 집어 넣고 방문 처리를 해주는 부분
            if board[nx][ny] == board[x][y] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

if __name__ == "__main__":
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 적록색약이 아닐 때
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                Bfs(i, j)
                cnt += 1
    
    # 줄바꿈X 공백 구분 위해 end=' ' 사용
    print(cnt, end=' ')

    # 적록색약일 때: G를 R로 변경해준 뒤 탐색
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'G':
                board[i][j] = 'R'

    # 방문 배열, 영역의 수 초기화
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                Bfs(i, j)
                cnt += 1

    print(cnt)