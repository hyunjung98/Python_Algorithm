from collections import deque

# 상하좌우 대각선 방향
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,-1,1,1,-1]

def dfs(x, y):
    # 위치 저장 후 데크에 넣고 방문처리
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    # 큐가 비어있지 않다면, 맨 뒤에 있는 값의 상하좌우, 대각선 탐색
    # 주변 좌표에 섬이 존재할 경우 큐에 넣고 방문 처리
    while q:
        x, y = q.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if board[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True

if __name__ == "__main__":
    while True:
        cnt = 0  # 섬의 개수
        w, h = map(int, input().split())    # 너비, 높이 입력
        board = [list(map(int, input().split())) for _ in range(h)]     # 지도 입력 받기
        visited = [[False] * w for _ in range(h)]   # 방문 체크 리스트
        
        # 입력값 '0 0'일 때 반복문 탈출
        if w == 0 and h == 0:
            break
        
        # 지도 탐색하며 섬이 있고, 방문하지 않았다면 dfs 실행 후 개수 증가
        for i in range(h):
            for j in range(w):
                if board[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    cnt += 1
        print(cnt)