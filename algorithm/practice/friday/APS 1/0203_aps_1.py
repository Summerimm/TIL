# 삼성시의 버스 노선
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    cnt = [0] * 5001 # 0~ 5000
    idx = [] # P 갯수만큼 들어오는 index 넣는 배열
    ans = [] # 정답 배열

    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            cnt[j] += 1 # 카운트 배열에 넣기

    p = int(input())
    for i in range(p):
        idx.append(int(input())) # index 배열에 적어넣기

    for index in idx:
        ans.append(cnt[index]) # 정답 배열에 노선 count 개수만큼 넣기

    answer = ' '.join(map(str, ans))
    print(f'#{tc+1} {answer}')