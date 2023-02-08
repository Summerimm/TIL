import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    s = input()
    s = s[::-1].translate(str.maketrans('pqbd', 'qpdb'))
    print(f'#{tc} {s}')