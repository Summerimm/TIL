# 베이비진 게임
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