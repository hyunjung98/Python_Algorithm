from collections import deque;

#  상하좌우 방향벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 음식물 담을 리스트
result = []

def Bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 탐색 범위 제한
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 음식물 쓰레기가 있고 방문하지 않았다면 개수 증가
            if board[nx][ny] == '#' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt

if __name__ == "__main__":
    # N: 세로 M: 가로 K: 음식물 개수
    N, M, K = map(int, input().split())
    board = [['.'] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    # 음식물 위치 받아오기
    # r, c는 좌표이므로 배열의 인덱스를 받아오기 위해 -1 해준다
    for _ in range(K):
        r, c = map(int, input().split())
        board[r-1][c-1] = '#'

    for i in range(N):
        for j in range(M):
            # 음식물 있으면 배열에 음식물 개수 저장
            if board[i][j] == '#' and not visited[i][j]:
                result.append(Bfs(i, j))

    # 배열에서 가장 큰 음식물 출력
    print(max(result))
