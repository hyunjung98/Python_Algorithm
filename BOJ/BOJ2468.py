from collections import deque;

# 상하좌우 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 물에 잠기지 않은 영역의 수
cnt = 0

# 반복문을 돌면서 최대 영역을 저장하는 배열 -> max()사용하여 최대 영역 수 출력
arrArea = []

# Bfs 함수가 실행되면서 좌표를 데크에 저장
# 해당 좌표 방문 처리(True)
def Bfs(x, y, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    # 가장 앞부분부터 꺼내어 상하좌우 탐색
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 값이 맵 밖으로 벗어나면 실행 X
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 주변에 위치한 값이 매개변수로 받아온 높이보다 크거나 같고,
            # 방문하지 않았다면 큐에 저장하고 방문 처리 작업 진행
            if board[nx][ny] >= h and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 입력한 2차원 배열의 최소, 최대값
    mapMin = map(min, board)
    minHeight = min(map(min, board))

    print(mapMin)
    print(minHeight)

    
    maxHeight = max(map(max, board))

    # 높이의 값이 최소부터 최대일 때까지 반복문 실행 
    for h in range(minHeight, maxHeight + 1):
        # 방문 배열, 영역의 수 초기화 -> 방문 처리가 되어있으면 각 높이에 따른 Bfs 실행 불가
        visited = [[False] * N for _ in range(N)]
        cnt = 0

        # 배열의 크기만큼 반복문 돌면서 물에 잠기지 않고, 방문하지 않았다면 Bfs 실행하고 영역의 수 증가
        for i in range(N):
            for j in range(N):
                if board[i][j] >= h and not visited[i][j]:
                    Bfs(i, j, h)
                    visited[i][j] = True
                    cnt += 1
        arrArea.append(cnt)

    # 배열에 담긴 영역의 수 중 최대값 출력
    print(max(arrArea))