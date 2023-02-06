# 문제
# 1. 문자열을 전달 받아 해당 문자열의 정중앙 문자를 출력하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 출력하라.


string = input()
length = len(string)
if length % 2: # 길이가 홀수면
    print(string[length // 2])
else:
    print(string[length // 2 - 1], string[length // 2])
