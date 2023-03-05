# 후위표기법 변환
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = ['('] + list(input()) + [')']
    op = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}

    ans, st = [], []
    for c in arr:
        if c not in op.keys(): # 피연산자일 때
            ans.append(c)
        elif c == '(': # 시작
            st.append(c)
        elif c == ')': # 종료
            while st[-1] != '(':
                ans.append(st.pop())
        else:
            if op[st[-1]] < op[c]:
                st.append(c)
            else:
                while op[st[-1]] >= op[c]:
                    ans.append(st.pop())
                st.append(c)
    a = ''
    for c in ans:
        a += c
    print(f'#{tc} {a}')
