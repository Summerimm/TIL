# 숫자조작
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    mn, mx = ''.join(arr), ''.join(arr)

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if i == 0 and arr[j] == '0':
                continue
            arr[i], arr[j] = arr[j], arr[i]
            mn = min(mn, ''.join(arr))
            mx = max(mx, ''.join(arr))
            arr[i], arr[j] = arr[j], arr[i]
    print(f'#{tc} {mn} {mx}')