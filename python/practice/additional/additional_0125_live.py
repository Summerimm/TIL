# 주어진 문자열에서 숫자, 문자, 기호가
# 각각 몇 개인지를 판단하는 함수를 작성

def check(target_str):
    alpha, digit, symbol = 0, 0, 0 
    for c in target_str:
        if c.isdigit():
            digit += 1
        elif c.isalpha():
            alpha += 1
        else:
            symbol += 1
    return f'문자: {alpha}개, 숫자: {digit}개, 기호: {symbol}개'

print(check('HappyNewYear2023!?'))
# 문자: 12개, 숫자: 4개, 기호: 2개