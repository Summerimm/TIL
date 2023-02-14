import sys, copy
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    tc = int(input())
    # 사다리 양쪽 padding
    lad = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # 시작열 index 추출
    start = []
    for i in range(102):
        if lad[0][i] == 1:
            start.append(i)
    # 이동횟수 리스트
    cntlist = []
    mn = 10000
    for dj in start:
        di = 0 # 시작 행 초기화
        cnt = 0  # 이동횟수
        tmp = copy.deepcopy(lad) # ladder deepcopy
        while di < 100:
            tmp[di][dj] = 0
            if tmp[di][dj - 1] == 1:  # 왼쪽이 1
                dj -= 1
                cnt += 1
            elif tmp[di][dj + 1] == 1:  # 오른쪽이 1
                dj += 1
                cnt += 1
            else:
                di += 1
        cntlist.append(cnt)
    mn = min(cntlist)
    s = start[cntlist.index(mn)]
    print(f'#{tc} {s - 1}')