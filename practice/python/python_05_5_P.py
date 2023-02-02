# 문제
#  1. 영어의 접두사 in은 않다, 않은의 의미를 가지고 있다. 
#     접두사 in-은 발음을 쉽게 하려는 목적에서 바로 뒤에 나오는 철자에 따라 변화형이 나타나기도 하는데, 변화형의 기본원리는 아래와 같다.    
#       - 변화형의 기본 원리       
#         n 뒤에 나오는 철자가 b, m, p일 때, im-으로 변화.       
#         n 뒤에 나오는 철자가 l일때, il-로 변화       
#         n 뒤에 나오는 철자가 r일때, ir-로 변화
# 2. 아래와 같이 딕셔너리가 주어졌을 때, 제어문을 사용하여 반의어의 모음을 만들어라.
# 3. 완성된 반의어의 모음은 오름차순으로 정렬하여 출력하라.


words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

in_dict = {}

bmp = ['b', 'm', 'p']
for word, kor in words_dict.items():
    if word[0] in bmp:
        in_dict['im'+f'{word}'] = kor
    elif word[0] == 'l':
        in_dict['il'+f'{word}'] = kor
    elif word[0] == 'r':
        in_dict['ir'+f'{word}'] = kor
    else:
        in_dict['in'+f'{word}'] = kor

print(dict(sorted(in_dict.items(), key=lambda x: x[0])))
