"""
목표: 상대 팀 진영에 최대한 빨리 도착하기 (이동을 최대한 적게하기)
검은색 부분&게임 맵 바깥: 갈 수 없는 길 (0)
흰색 부분: 갈 수 있는 길 (1)
캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동, 처음 내 위치 (1,1) / 상대방 위치 (n,m)
상대팀 진영 주위에 검은색으로 둘러싸여 있다면 불가능 -> return -1
"""
from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)] # maps 형태대로 모든 칸에 false인 2차원 행렬, 방문 여부 기록
    
    queue = deque()
    # 시작 위치 큐에 추가 & 방문 기록
    queue.append((0,0))
    visited[0][0] = True
    
    # 큐가 비워질 때까지 반복
    while queue:
        # x가 행 (세로 방향), y가 열 (가로 방향)
        x, y = queue.popleft()
        # 이동할 수 있는 동서남북 경우
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 게임 맵 바깥이라면 그냥 넘어가기
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 하얀색 칸 & 아직 방문 전
            elif maps[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
    
    res = maps[n-1][m-1]
    return res if res > 1 else -1