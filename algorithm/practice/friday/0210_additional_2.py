import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}')
    n = int(input())
    nlist = [list(map(int, input().split())) for _ in range(n)]

    # 90도 회전(ans1), 180도 회전(ans2), 270도 회전(ans3)
    for i in range(n):
        ans1, ans2, ans3 = '', '', ''
        for j in range(n):
            s1 = nlist[n-1-j][i]
            s2 = nlist[n-1-i][n-1-j]
            s3 = nlist[j][n-1-i]
            ans1 += str(s1)
            ans2 += str(s2)
            ans3 += str(s3)
        print(ans1, ans2, ans3)