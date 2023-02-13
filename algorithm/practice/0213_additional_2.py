# 비밀번호
import sys
sys.stdin = open('input.txt.', 'r')

for tc in range(1, 11):
    l, nums = map(str, input().split())
    st = []
    for n in nums:
        if st and n == st[-1]:
            st.pop()
        else:
            st.append(n)
    ans = ''.join(map(str, st))
    print(f'#{tc} {ans}')