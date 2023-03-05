# Forth
# 후위표기식
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))
    op = ['+', '*', '/', '-']
    st = []
    if '.' not in arr: # . 없을 경우
        ans = 'error'
    else: # . 있을 경우
        for idx, c in enumerate(arr):
            try:
                if c in op: # 연산자일 때
                    n1, n2 = int(st.pop()), int(st.pop())
                    if c == '+': 
                        st.append(n2 + n1)
                    elif c == '-':
                        st.append(n2 - n1)
                    elif c == '*':
                        st.append(n2 * n1)
                    else:
                        st.append(n2 // n1)
                elif c == '.' and idx == len(arr)-1 and len(st) == 1:
                    # 가장 마지막에 있는 마침표이고 스택에 숫자가 하나뿐임
                    ans = st.pop()
                    break
                elif c == '.': 
                    # 마침표이고 스택에 숫자 여러개(or 0개)거나 마지막에 있는 마침표가 아니거나
                    ans = 'error'
                    break
                else: # 피연산자일 때
                    st.append(c)
            except: # pop 못하면
                ans = 'error'
                break
    print(f'#{tc} {ans}')