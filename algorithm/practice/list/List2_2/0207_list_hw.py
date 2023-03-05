# Ladder1
import sys
sys.stdin = open('input.txt', 'r')

for _ in range(1,  4): # 11
    tc = int(input())
    dj = [-1, 1] # 좌, 우(열)
    ladder = []
    for _ in range(100): 
        ladder.append(list(map(int, input().split())))
    dst = ladder[99].index(2)

    pos = 98 # 행 
    while pos > 0: # 1
        if ladder[pos-1][dst] == 0: # 다리 지나가는 중(위를 보면 0일 때)
            ladder[pos][dst] = 2
            dst += dk
        else: # 같은 열(위를 봐도 1일 때)
            for k in range(2):
                tmp = dst + dj[k] # 8 10
                if 0 <= tmp < 100 and ladder[pos][tmp] == 1: # 옆에 1이 있으면
                    ladder[pos][dst] += 1 # 출발한 지점 1을 2로 바꿈
                    dst = tmp # 열을 바꾸고
                    dk = dj[k] # 방향을 저장해놓음
                    break
            else: # 옆에 1이 없으면
                # ladder[pos][dst] += 1 # 2로 바꾸고
                pos -= 1 # 행을 위로 올림
    print(f'#{tc} {dst}')