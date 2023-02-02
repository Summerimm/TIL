# 문제
# 1. 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를 작성하시오.

def count_vowels(string):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for c in string:
        if c in vowel_list:
            cnt += 1
    return cnt


count_vowels('apple') #=> 2
count_vowels('banana') #=> 3