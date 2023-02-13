# 괄호검사2
import sys
sys.stdin = open('input.txt.', 'r')

T = int(input())
for tc in range(1, T+1):
    ans = 0
    a = list(input())
    lst = ['(', ')', '{', '}']
    p, st = [], []
    for c in a:
        if c in lst:
            p.append(c)
    for c in p:
        if c == '(':
            st.append(c)
        elif c == '{':
            st.append(c)
        elif c == '}' and (st == [] or st[-1] == '('):
            st.append(c)
            break
        elif c == ')' and (st == [] or st[-1] == '{'):
            st.append(c)
            break
        elif c == ')' and st[-1] == '(':
            st.pop()
        elif c == '}' and st[-1] == '{':
            st.pop()
    if st == []:
        ans = 1
    print(f'#{tc} {ans}')