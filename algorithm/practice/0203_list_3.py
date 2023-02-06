# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.

# 입력
# 첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N, 다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공된다.
# 1<=T<=10, 10<=N<=1000

# 출력
# #과 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    seq = input().split('0')
    ans = 0
    for s in seq:
        if len(s) > ans:
            ans = len(s)
    print(f'#{tc+1} {ans}')
