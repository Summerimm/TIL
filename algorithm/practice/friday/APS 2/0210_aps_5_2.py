# 회문2_sol
import sys
sys.stdin = open('input.txt', 'r')

def isPal(arr, m):
    for lst in arr: # 한 줄씩 가져오기
        for i in range(n - m + 1):
            # [2] 인덱스로 절반만 비교
            for j in range(m // 2):
                if lst[i+j] != lst[i+m-1-j]:
                    break
            else:
                return True
            # [1] 슬라이싱 사용
            # if lst[i:i+m] == lst[i:i+m][::-1]:
            #     return True
            # else:
            #     return True
    return False

T = 10
for tc in range(1, T + 1):
    t = int(input())
    n = 100
    arr = [input() for _ in range(n)]
    # arr_t = list(zip(*arr)) # separate된 문자들을 tuple형태로 list에 넣음
    arr_t = ["".join(x) for x in zip(*arr)] # 문자열을 list에 넣음/arr과 동일구조

    for m in range(n, 1, -1):
        if isPal(arr, m) or isPal(arr_t, m):
            break
    else:
        m = 1
    print(f'#{tc} {m}')