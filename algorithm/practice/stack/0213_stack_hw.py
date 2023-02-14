# 파스칼의 삼각형
import sys
sys.stdin = open('input.txt.', 'r')


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    n = int(input())
    st, tmp = [], []
    for i in range(n):
        if i < 2:
            st.append(1)
        else:
            tmp = []
            for j in range(len(st)-1):
                tmp.append(st[j] + st[j+1])
            st = [1, *tmp, 1]
        print(*st)