# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

# [입력]
# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

# [출력]
# #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다

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