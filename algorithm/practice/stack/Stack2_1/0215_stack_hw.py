# 계산기 1
import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    l = int(input())
    arr = list(input())
    st = []
    eq = [] # 후위표기식

    # 후위표기식 변환
    for c in arr:
        if c == '+' and st == []:
            st.append(c)
        elif c == '+':
            eq.append(st.pop())
            st.append(c)
        else:
            eq.append(c)
    eq.append(st.pop())
    
    # 후위표기식 계산
    for c in eq:
        if c == '+':
            n1, n2 = int(st.pop()), int(st.pop())
            st.append(n1 + n2)
        else:
            st.append(c)
    ans = st.pop()
    print(f'#{tc} {ans}')