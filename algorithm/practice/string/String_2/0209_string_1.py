# String
import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

for t in range(1, 11):
    tc = int(input())
    p = input()
    t = input()

    n = len(t)
    m = len(p)
    ans = 0
    for i in range(0, n - m + 1):
        if p == t[i:i + m]:
            ans += 1
    print(f'#{tc} {ans}')
