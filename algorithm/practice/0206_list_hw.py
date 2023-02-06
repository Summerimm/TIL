import sys
sys.stdin = open('input.txt', 'r')

for _ in range(1, 3): #############
    t = int(input())
    a = [list(map(int, input().split())) for _ in range(100)]
    asumlist = []
    # 행, 열, 대각선
    for i in range(100):
        asumc, asumr, asum1, asum2 = 0, 0, 0, 0
        for j in range(100):
            asumr += a[i][j]
            asumc += a[j][i]
            if i == j:
                asum1 += a[i][j]
                asum2 += a[i][99 - j]
        asumlist.append(asumr)
        asumlist.append(asumc)
        asumlist.append(asum1)
        asumlist.append(asum2)
    print(f'#{t} {max(asumlist)}')