from collections import deque;

# 상하좌우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 병사의 수
cnt = 0

# 병사의 옷 색 (W, B)
color = ''

# 아군, 적군의 위력으로 제곱해서 더할 변수
blue = 0
white = 0

def bfs(x, y, color):
    # 현재 들어온 병사를 큐에 넣기 때문에 병사의 수(cnt)를 1로 시작
    # 방문 처리 위해 현재 좌표값을 True로 변경
    # 큐에 넣은 좌표값을 꺼내어 상하좌우 탐색 -> 해당 값이 있고 방문하지 않았다면, 큐에 넣고 병사의 수 증가
    # 병사 n명 뭉쳐있을 경우 제곱의 위력 -> cnt^2 반환 
    cnt = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == color and not visited[nx][ny]:
                q.append((nx, ny))
                cnt += 1
                visited[nx][ny] = True  
    return cnt ** 2

if __name__ == "__main__":
    n, m = map(int, input().split())                        # 가로 세로 입력
    board = [list(input().strip()) for _ in range(m)]       # 병사의 옷 색 공백 없이 입력 받아 2차원 리스트 생성 
    visited = [[False] * n for _ in range(m)]               # 방문 확인 리스트

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'W' and not visited[i][j]:    # 값이 'W'이고 방문하지 않았을 때 BFS 실행
                color = board[i][j]
                white += bfs(i, j, color)                   # 하얀 옷을 입은 병사의 위력 저장

            elif board[i][j] == 'B' and not visited[i][j]:  # 값이 'B'이고 방문하지 않았을 때 BFS 실행
                color = board[i][j]
                blue += bfs(i, j, color)                    # 파란 옷을 입은 병사의 위력 저장

print(white, blue)