# 미생물 격리
import sys
sys.stdin = open('input.txt', 'r')

dic = {1:2, 2:1, 3:4, 4:3}
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    
    # M번만큼 반복해서 처리
    for _ in range(M):
        for k in range(len(arr)):       # arr의 크기가 바뀔 수 있음
            arr[k][0] += di[arr[k][3]]
            arr[k][1] += dj[arr[k][3]]
            ni, nj = arr[k][0], arr[k][1]
            if ni == 0 or ni == N-1 or nj == 0 or nj == N-1:
                n = arr[k][2] // 2
                d = dic[arr[k][3]]
            else:
                n = arr[k][2]
                d = arr[k][3]
            arr[k] = [ni, nj, n, d]
        
        # 세로좌표, 가로좌표, 미생물 수 -> 내림차순으로 정렬 후 같은 좌표 합치기
        arr.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
        i = 1
        while i < len(arr):
            if arr[i-1][:2] == arr[i][:2]:  # 같은 좌표면
                arr[i-1][2] += arr[i][2]    # 미생물 수가 많은 쪽에 합치고
                arr.pop(i)  # 인덱스로 빼내기
            else:
                i += 1      # 같은 좌표 아니면 인덱스 늘리기
    
    ans = 0
    for lst in arr:
        ans += lst[2]       
    print(f'#{tc} {ans}')