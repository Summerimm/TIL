# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

numlist = list(map(int, input().split()))
anslist = []

for idx, num in enumerate(numlist):
    if idx == 0:
        anslist.append(num)
    else:
        if num != numlist[idx - 1]:
            anslist.append(num)

print(anslist)
