# 반복문자 지우기
import sys
sys.stdin = open('input.txt.', 'r')

T = int(input())
for tc in range(1, T+1):
    p = list(input())
    st = []

    for c in p:
        if st == []:
            st.append(c)
        elif c == st[-1]:
            st.pop()
        else:
            st.append(c)
    ans = len(st)
    print(f'#{tc} {ans}')