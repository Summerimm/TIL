# 단순 2진 암호코드
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    for n in range(N):
        c = input()
        if '1' not in c:
            continue
        else:
            secret = c

    for idx in range(M-1, -1, -1):
        if secret[idx] == '1':
            real = secret[idx-55:idx+1]
            break

    nums = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
            '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}
    pwd = ''
    for i in range(8):
        if real[7*i:7*i+7] in nums.keys():
            pwd += nums[real[7*i:7*i+7]]

    odd, even = 0, 0
    for i in range(7):
        if i % 2:
            even += int(pwd[i])
        else:
            odd += int(pwd[i])

    if (odd * 3 + even + int(pwd[-1])) % 10 == 0:
        ans = odd + even + int(pwd[-1])
    else:
        ans = 0

    print(f'#{tc} {ans}')