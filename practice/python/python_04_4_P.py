# 문제
# 아스키 코드는 미국 ANSI에서 표준화한 정보교환용 7비트 부호체계이다. 
# 아스키 코드는 총 128가지의 문자를 나타낼 수 있으며 각각의 문자를 나타내는 숫자값이 존재한다. 
# Python에서는 built-in 함수인 ord()와 chr()을 사용하여, 
# 각각 아스키 코드 인코딩에 대응되는 숫자와 문자로 변환할 수 있다.
# 문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 더 큰 합을 가진 문자열을 반환하는 코드를 작성하시오

word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

sum1, sum2 = 0, 0

for d in word1:
    sum1 += ord(d)
for d in word2:
    sum2 += ord(d)

if sum1 > sum2:
    print(word1)
elif sum2 > sum1 :
    print(word2)
else:
    print(word1, word2)
