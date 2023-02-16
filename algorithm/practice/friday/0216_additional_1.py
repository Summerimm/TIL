# 고대 유적
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arrt = list(zip(*arr))      # 전치행렬

    # 스택을 이용해서 1이 나오면 push, 0이 나오면 길이 2이상 후보군에 넣고 clear
    # for문 끝나면 남은 스택의 길이 2이상 일때 후보군에 넣기
    cand = []
    for i in range(N):
        st1, st2 = [], []
        for n1 in arr[i]:
            if n1 == 0:                     # 그림의 숫자가 0
                if len(st1) >= 2:
                    cand.append(len(st1))
                st1.clear()
            else:                           # 그림의 숫자가 1
                st1.append(n1)
        if len(st1) >= 2:
            cand.append(len(st1))

        for n2 in arrt[i]:
            if n2 == 0:                     # 그림의 숫자가 0
                if len(st2) >= 2:
                    cand.append(len(st2))
                st2.clear()
            else:                           # 그림의 숫자가 1
                st2.append(n2)
        if len(st2) >= 2:
            cand.append(len(st2))

    print(f'#{tc} {max(cand)}')