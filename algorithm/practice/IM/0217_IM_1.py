# 원재의 메모리 복구하기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    nums = input()
    N = len(nums)
    ans = 0

    for i in range(N):
        if nums[i] == '1':
            idx = i # 처음으로 1이 되는 인덱스
            break
    st = ['1']

    for j in range(i, N):
        if st[-1] == nums[j]:
            st.append(nums[j])
        else:
            while st:
                st.pop()
            st.append(nums[j])
            ans += 1
    ans += 1
    print(f'#{tc} {ans}')