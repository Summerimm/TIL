# 문제
# 1.  사용자가 입력한 숫자의 각 자릿수를 더해 출력하는 sum_of_digit를 작성하라.      
# 단, 반복문을 활용하지 않는 코드로 작성하라.      
# 단, 반복문을 활용한 방법과 반복문을 활용하지 않은 방법을 두 가지 모두 작성하라. 
# A. 입력 예시
# sum_of_digit(3904) # 16

def sum_of_digit(num): # 재귀함수 사용
    if num < 10:
        sum = num
        return sum
    else:
        rem = num % 10
        num = num // 10
        sum = sum_of_digit(num)
        sum += rem
        return sum

def sum_of_digit2(num): # 반복문 사용
    sum = 0
    numlist = list(str(num))
    for i in numlist:
        sum += int(i)
    return sum

#---------------------------------------
def sum_of_digit_ans(number):
    print(number)
    number = str(number)
    if number == '':
        return 0
    return sum_of_digit_ans(number[:-1]) + int(number[-1])

def sum_of_digit_ans2(number):
    quotient = number // 10
    remainder = number % 10
    if quotient == 0:
        return remainder
    return sum_of_digit_ans2(quotient) + remainder

print(sum_of_digit_ans2(3904)) # 16