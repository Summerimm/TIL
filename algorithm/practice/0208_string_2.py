import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    ans = 1
    if str2.find(str1) == -1:
        ans = 0
    print(f'#{tc} {ans}')