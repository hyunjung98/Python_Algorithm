from collections import deque;

#  상하좌우 방향벡터
dx = [0,0,1,-1]
dy = [1,-1,0,0]

result = []     # 영역의 개수를 담는 리스트
cnt = 0         # 분리 영역 개수

# dfs를 실행될 때마다 분리된 영역 개수(cnt) 증가
# 해당 x, y 값 데크에 저장하고 방문 처리(False -> True)
def Dfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    # 큐가 비어있지 않다면, 해당 좌표의 상하좌우를 탐색
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 배열 인덱스를 넘지 않도록 범위 설정
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            # 탐색한 4방향의 값이 1이고 방문 리스트가 False일 경우 데크에 좌표값 저장 후 방문 처리, 영역 개수 증가
            if board[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return result.append(cnt)   # 오름차순 정렬 위해 영역 개수 리스트에 담고 반환

if __name__ == "__main__":
    # N: 가로 M: 세로 K: 분리 영역 개수(0으로 채울 부분)
    # 입력은 세로, 가로(M, N)를 받음

    M, N ,K = map(int, input().split())
    board = [[1] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    # 분리할 영역 0으로 채우기
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(y1, y2):
            for j in range(x1, x2):
                board[i][j] = 0

    # 해당 좌표가 1이고 방문하지 않았으면 DFS 실행 후 영역 수 증가시키기
    for i in range(M):
        for j in range(N):
            if board[i][j] == 1 and not visited[i][j]:
                Dfs(i ,j)
                cnt += 1


# 오름차순 정렬
result.sort()

print(cnt)      # 3

for i in result:
    print(i, end=' ')   # 1 7 13
