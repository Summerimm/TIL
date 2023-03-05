# 백만장자 프로젝트
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    print(nums)
    st = []
    mx, s = 0, 0
    for i, n in enumerate(nums):
        if n > mx:
            mx = n
            if st and (i == len(nums) - 1 or nums[i+1] < n): # local maximum
                s += mx - st.pop()
                mx = 0
            else:
                st.append(n)
        else:
            st.append(n)
        
        
    # print(f'#{tc} {s}')