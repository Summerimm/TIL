# 새로운 버스 노선
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(T):
    N = int(input()) # 노선의 수
    cnt = [0] * 1001 # 0~1000
    for i in range(N):
        tp, A, B = map(int, input().split()) 
        if tp == 1:
            for idx in range(A+1, B):
                cnt[idx] += 1

        elif tp == 2:
            if A % 2 == 0:
                for idx in range(A+1, B):
                    if idx % 2 == 0:
                        cnt[idx] += 1
            else:
                for idx in range(A+1, B):
                    if idx % 2 == 1:
                        cnt[idx] += 1

        elif tp == 3:
            if A % 2 == 0:
                for idx in range(A+1, B):
                    if idx % 4 == 0:
                        cnt[idx] += 1
            else:
                for idx in range(A+1, B):
                    if idx % 3 == 0 and idx % 10 != 0:
                        cnt[idx] += 1
        cnt[A] += 1
        cnt[B] += 1

    ans = max(cnt)
    print(f'#{tc+1}', ans)