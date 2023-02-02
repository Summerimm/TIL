# 문제
# 여러 개의 소금물을 섞었을 때, 혼합된 소금물의 퍼센트 농도와 양을 계산하는 프로그램을 만드시오.

# 조건
# 소금물의 퍼센트 농도와 소금물의 양을 입력하고, Done을 입력하면 혼합물의 퍼센트 농도와 양이 출력되도록 하시오. 
# 최대 5개의 소금물을 입력할 수 있다. 
# 출력된 혼합물의 퍼센트 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여 2번째 자리까지만 나타내시오.

import sys

sys.stdin = open('input.txt', 'r')

salt_sum = 0
total_percent, total_sum = 0, 0

while True:
    tmp = input()
    if tmp == 'Done':
        break
    else:
        percent, quantity = map(float, tmp.split())
        salt_sum += 0.01 * percent * quantity
        total_sum += quantity

total_percent = salt_sum / total_sum * 100
print(round(total_percent, 2), round(total_sum, 2))




