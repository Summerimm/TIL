# 문제
# # 문자열 s를 아래와 같이 수정하고, 출력하라.

# 요구사항
# 모든 대문자는 소문자로 바꾸되, 가장 첫 번째 대문자 I는 바꾸지 않는다.
# 문자열 앞뒤에 있는 특수 문자를 삭제한다.

# 입력 예시
# @#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!
# 출력 예시
# 'I never dreamed about success, i worked for it.'

s = input()
s = s.strip('@''#''~''!''>')
s = s.lower()
s = s.replace(s[0], s[0].upper())
print(s)