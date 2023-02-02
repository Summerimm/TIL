# 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 
# 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고,
# 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
# 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.

# 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.

# 667767은 두 개의 triplet이므로 baby-gin이다. (666, 777)
# 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin이다. (456, 000)
# 101123은 한 개의 triplet가 존재하나, 023이 run이 아니므로 baby-gin 이 아니다.
# (123을 run으로 사용하더라도 011이 run이나 triplet가 아님)

import sys
sys.stdin = open('input.txt', 'r')

# Brute-force
def babygin(num):
    for i1 in range(6):
        for i2 in range(6):
            if i2 != i1:
                for i3 in range(6):
                    if i3 != i2 and i3 != i1:
                        for i4 in range(6):
                            if i4 != i3 and i4 != i2 and i4 != i1:
                                for i5 in range(6):
                                    if i5 != i4 and i5 != i3 and i5 != i2 and i5 != i1:
                                        for i6 in range(6):
                                            if i6 != i5 and i6 != i4 and i6 != i3 and i6 != i2 and i6 != i1:
                                                if int(num[i1]) == int(num[i2]) == int(num[i3]):
                                                    if int(num[i4]) == int(num[i5]) == int(num[i6]):
                                                        return 1
                                                    elif int(num[i6]) == int(num[i5]) + 1 and int(num[i5]) == int(num[i4]) + 1:
                                                        return 1
                                                elif int(num[i3]) == int(num[i2]) + 1 and int(num[i2]) == int(num[i1]) + 1:
                                                    if int(num[i4]) == int(num[i5]) == int(num[i6]):
                                                        return 1
                                                    elif int(num[i6]) == int(num[i5]) + 1 and int(num[i5]) == int(num[i4]) + 1:
                                                        return 1
    return 0

T = int(input())
for tc in range(T):
    num = input()
    ans = babygin(num)
    print(f'#{tc+1} {ans}')