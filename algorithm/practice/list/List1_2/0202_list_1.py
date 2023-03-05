# 정렬 연습
import sys
sys.stdin = open('input.txt', 'r')

# Counting Sort
T = int(input())
for tc in range(T):
    n = int(input()) # origin 배열 길이
    origin = list(map(int, input().split()))
    sortlist = [0] * n # 정렬된 배열 길이
    cnt = [0] * 101 # 최대 정수 0 ~ 100

    for i in range(n):
        cnt[origin[i]] += 1 # 각 index 숫자가 몇 개 있는지

    for i in range(1, 101):
        cnt[i] += cnt[i - 1] # 누적합 배열로 변환

    for i in range(n):
        cnt[origin[i]] -= 1 # 정렬된 배열 인덱스
        sortlist[cnt[origin[i]]] = origin[i]

    ans = (str(sortlist).strip('['']')).replace(',','')
    print(f'#{tc+1} {ans}')