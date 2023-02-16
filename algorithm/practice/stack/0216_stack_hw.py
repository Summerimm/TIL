# 계산기2
import sys
sys.stdin = open('input.txt', 'r')

op = {'+': 0, '*': 1}
T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = input()
    
    # 후위표기식으로 변환
    st = []
    eq = ''
    for c in arr:
        if c.isdigit():
            eq += c
        else:
            while st and op[c] <= op[st[-1]]:
                eq += st.pop()
            st.append(c)
    # 스택에 남아있는 데이터 처리
    while st:
        eq += st.pop()

    # 후위표기식 연산
    for c in eq:
        if c.isdigit():
            st.append(int(c))
        else:
            n1, n2 = int(st.pop()), int(st.pop())
            if c == '*':
                st.append(n2 * n1)
            else:
                st.append(n2 + n1)
    ans = st.pop()
    print(f'#{tc} {ans}')