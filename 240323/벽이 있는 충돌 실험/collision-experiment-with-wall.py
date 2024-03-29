def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def move_marbles(N, M, count, marbles, dy, dx):
    # 구슬의 수가 지정한 방향으로 격자를 한 번 왕복할 때까지 변하지 않으면 정지
    unchange_cnt = 0
    while unchange_cnt < N * 2:
        # 남아있는 구슬 이동
        for i in range(M):
            r, c, d = marbles[i]
            nr, nc = r + dy[d], c + dx[d]
            if not in_range(nr, nc, N, N):
                marbles[i][2] = (d + 2) % 4
            else:
                count[nr][nc] += 1
                count[r][c] -= 1
                marbles[i][0], marbles[i][1] = nr, nc

        # 남아있는 구슬 이동 후 한 칸에 2개 이상 있는 구슬 제거
        sig = False # 구슬 수 변화하는 않은 상태로 초기화, 만일 변화하면 True 전환
        for i in range(N):
            for j in range(N):
                if count[i][j] >= 2:
                    count[i][j] = 0
                    # marbles 리스트에서 조건에 해당하는 구슬 제거, 해당 구슬을 맨 뒤로 보낸 후 pop() -> O(n) 시간복잡도로 제거를 위해
                    m_idx = 0   # m_idx는 marble내 인덱스, 제거되는 구슬이 있으면 증가하지 않고 제거되는 구슬이 없을 때만 제거
                    while m_idx < M:
                        if marbles[m_idx][0] == i and marbles[m_idx][1] == j:
                            marbles[m_idx], marbles[-1] = marbles[-1], marbles[m_idx]
                            marbles.pop()
                            M -= 1
                            unchange_cnt = 0    # 구슬을 제거하면 구슬의 수가 변하므로 구슬 수가 변화하지 않은 시간이 0으로 초기화
                            sig = True
                            continue
                        m_idx += 1
        if not sig: unchange_cnt += 1
    return M

T = int(input())
# 테스트 케이스 실행
dir_dict = {'U' : 0, 'D' : 2, 'R' : 1, 'L' : 3}
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
for _ in range(T):
    N, M = [int(x) for x in input().split()]
    marbles = [input().split() for _ in range(M)]

    # count 배열 초기화 및 입력으로 들어온 marbles 요소를 정수로 변환
    count = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(M):
        r, c, d = int(marbles[i][0]) - 1, int(marbles[i][1]) - 1, dir_dict[marbles[i][2]]
        marbles[i] = [r, c, d]
        count[r][c] += 1
    
    exist_m = move_marbles(N, M, count, marbles, dy, dx)
    print(exist_m)