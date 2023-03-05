# 계산기3
import sys
sys.stdin = open('input.txt', 'r')

op = {'+': 1, '*': 2, '(': 0}
T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = list(input())

    # 후위표기식 변환
    st = []
    eq = ''
    for c in arr:
        if c.isdigit():
            eq += c
        elif c == '(':
            st.append(c)
        elif c == ')':
            while st[-1] != '(':
                eq += st.pop()
            st.pop()    # 스택에 ( 남아있기 때문
        else:
            while st and op[c] <= op[st[-1]]:
                eq += st.pop()
            st.append(c)
    while st:
        eq += st.pop()

    # 후위표기식 계산
    for c in eq:
        if c.isdigit():
            st.append(c)
        else:
            n1 = int(st.pop())
            n2 = int(st.pop())
            if c == '*':
                st.append(n1 * n2)
            else:
                st.append(n1 + n2)
    ans = st.pop()
    print(f'#{tc} {ans}')