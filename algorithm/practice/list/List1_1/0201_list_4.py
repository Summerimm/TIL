# 정렬 연습
T = int(input())
for tc in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    num = str(nums).strip('['']')
    num = num.replace(',','')
    print(f'#{tc+1} {num}')