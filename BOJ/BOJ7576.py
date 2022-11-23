from collections import deque;

# 상하좌우 방향 벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

check = 0   # 익지 않은 토마토(0)가 있다면 1을 넘겨줌
max = 0     # 최대 일수

def Bfs():
    # 값이 1인 곳의 상하좌우 탐색
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 해당 위치의 상하좌우의 값이 0(익지 않은 토마토)일 때 해당 값을 증가시켜서 최대 일수를 구함
            if board[nx][ny] == 0:
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1

if __name__ == "__main__":
    # M: 가로, N: 세로
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    q = deque()

    # 맵에서 1인 곳을 찾아 큐에 담고 BFS 실행
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                q.append((i, j))

    Bfs()

    # BFS가 끝난 후 2차원 배열에 0이 존재할 경우 
    for i in range(N):
        for j in range(M):
            # 익지 않은 토마토가 있으면 check 변수에 1 담고 이 값이 1일 때 -1 출력
            if board[i][j] == 0:
                check = 1
            
            # 가장 큰 값 max 변수에 담기
            if max < board[i][j]:
                max = board[i][j]

    # 출력하는 부분
    if check == 1:
        print(-1)
    else:
        print(max-1)