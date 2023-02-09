import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    t, p = input().split()
    tlen = len(t)
    plen = len(p)

    cnt = 0
    i = 0
    if tlen >= plen:
        while i <= tlen:
            if p == t[i:i+plen]:
                cnt += 1
                i = i + plen
            else:
                i += 1  
        ans = tlen - plen * cnt + cnt
    else:
        ans = 0
    print(f'#{tc} {ans}')