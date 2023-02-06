# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

# [제약 사항]
# N 은 5 이상 50 이하이며, 
# 0이상 100이하의 값으로 구성되어 있다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.
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