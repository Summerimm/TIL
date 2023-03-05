# 쇠막대기 자르기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    p = list(input())
    st = []
    ans = 0
    for i, c in enumerate(p):
        if c == '(':
            st.append(c)
        elif c == ')' and st[-1] == p[i-1] == '(': # 레이저
            st.pop()
            ans += len(st)
        elif c == ')' and p[i-1] == ')': # 쇠막대기의 끝
            st.pop()
            ans += 1
    print(f'#{tc} {ans}')