# [파이썬 S/W 문제해결 기본] 1일차 - 전기버스
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))
    charge.append(n)
    print(k, n, m, charge)
    ans = 0
    tmp = 0 # 들린 정류장의 인덱스

    for i in range(len(charge)-1):
        if charge[0] > k or charge[i+1] - charge[i] > k: # 첫 충전소가 k보다 크거나 충전기 정류소 간 거리가 k보다 클 때
            ans = 0
            break
        else: # 충전소 간 거리는 k보다 작을 때
            if charge[i] == tmp + k:
                ans += 1
                tmp = charge[i]
            elif charge[i] < tmp + k and charge[i+1] > tmp + k:
                ans += 1
                tmp = charge[i]

    print(f'#{tc+1} {ans}')