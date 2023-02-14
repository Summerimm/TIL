# 괄호검사
import sys
sys.stdin = open('input.txt.', 'r')

T = int(input())
for tc in range(1, T+1):
    ans = 0
    p = list(input())
    st = []
    for c in p:
        if c == '(':
            st.append(c)
        elif c == ')' and st == []:
            st.append(c)
            break
        elif c == ')' and st[-1] == '(':
            st.pop()
    if st == []:
        ans = 1
    print(f'#{tc} {ans}')