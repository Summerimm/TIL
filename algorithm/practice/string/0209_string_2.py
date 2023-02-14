import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for tc in range(1, T + 1):
    p = input()
    t = input()
    d = {}
    for c in p:
        d[c] = 0
    for c in t:
        if c in d:
            d[c] += 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(f'#{tc} {d[0][1]}')
