from collections import deque

# 상하좌우 방향벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 넓이 저장 배열
result = []

# 그림의 개수
cnt = 0

def Dfs(x, y):
    area = 1                # 그림의 넓이
    q = deque()
    q.append((x, y))        # 좌표 데크에 넣어 저장
    visited[x][y] = True    # 방문 처리


    while q:
        x, y = q.pop()
        # 상하좌우 탐색해서 그림이 존재하면 데크에 위치값 저장 후 그림 넓이 1 증가
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if board[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                area += 1
    return area


if __name__ == "__main__":
    # r: 열, c: 행
    r, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]     # 한줄씩 값 채워넣기
    visited = [[False] * c for _ in range(r)]                       # 방문 배열

    for i in range(r):
        for j in range(c):
            if board[i][j] == 1 and not visited[i][j]:
                result.append(Dfs(i, j))                # 그림 넓이 저장
                cnt += 1                                # 그림 개수 증가
                visited[i][j] = True                    # 방문 처리
    
    # 그림이 없을 때는 그림의 넓이를 0으로 처리
    if len(result) == 0:
        print(0)
        print(0)
    else:
        print(cnt)
        print(max(result))