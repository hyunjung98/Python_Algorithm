from collections import deque

N = int(input())

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = [] 
cnt = 0

def bfs(x, y):
    # bfs 실행 시 현재 위치의 값이 1이기 때문에 단지내 집의 수(cnt) 1로 설정
    # 데크 생성하여 단지가 있는(1) 위치 저장
    # 방문 처리를 위해 현재 위치값 0으로 변경
    cnt = 1
    q = deque()
    q.append((x, y))
    board[x][y] = 0

    # 상하좌우 탐색하여 해당 위치의 값이 1일 경우 데크에 위치 저장 후 단지내 집의 수 증가
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 1 :
                    board[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1

    # 데크가 비었을 경우, 리스트에 단지내 집의 수 저장
    result.append(cnt)

if __name__ == "__main__":
    board = []
    for _ in range(N):
        board.append(list(map(int, input())))

    # 지도의 값이 1일 때, bfs 실행하고, 단지수 출력 위해 bfs 실행 횟수 cnt에 저장
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                bfs(i, j)
                cnt += 1

# 오름차순 정렬
result.sort()

# 단지 모임 출력
print(cnt)

# 단지수 출력
for i in result:
    print(i)