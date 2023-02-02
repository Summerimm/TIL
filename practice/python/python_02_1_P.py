# 문제
# 아래는 이차방정식의 근을 찾은 근의 공식이다. 
# 다음 a,b,c를 가지고 이차 방정식을 작성하고, 이차방정식의 근을 튜플 형식으로 출력하라. (소수점 4번째 자리에서 반올림하라.)

import math

a = 3
b = 6
c = - 5
x = 3

quad_eq = a * (x**2) + b * x + c
formula1 = round((- b + math.sqrt(b**2-4*a*c)) / (2 * a), 3)
formula2 = round((- b - math.sqrt(b**2-4*a*c)) / (2 * a), 3)
ans = (formula1, formula2)
print(formula1)
print(ans)