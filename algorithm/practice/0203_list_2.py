# 숫자 N은 아래와 같다.
# N=2^a x 3^b x 5^c x 7^d x 11^e
# N이 주어질 때 a, b, c, d, e 를 출력하라.

# [제약 사항]
# N은 2 이상 10,000,000 이하이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while(n != 1):
        if n % 11 == 0:
            e += 1
            n //= 11
        elif n % 7 == 0:
            d += 1
            n //= 7
        elif n % 5 == 0:
            c += 1
            n //= 5
        elif n % 3 == 0:
            b += 1
            n //= 3
        elif n % 2 == 0:
            a += 1
            n //= 2

    print(f'#{tc+1} {a} {b} {c} {d} {e}')