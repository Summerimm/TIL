# 목표
# 학습주제
# 파이썬 개발 환경에 대한 이해
# 파이썬 예외처리 기본 방식에 대한 이해

# 학습목표
# 모듈 동작 방식에 대해 이해한다.
# 파이썬 자료 구조의 구조 및 동작 방식에 대해 이해한다.
# 예외처리 방식 및 활용 방식에 대해 이해한다.

# 문제
# 연도, 월, 일을 순서대로 입력받는다.
# 윤년으로 가면 타임머신에 에러가 생긴다. 윤년을 입력했을 경우 연도를 다시 입력받아야 한다.
# 윤년이 아닌 연도를 입력받을 경우, 날짜를 편하게 정할 수 있도록 해당 연도의 달력을 출력하라.
# 김코딩은 월요일을 싫어한다. 입력한 날짜가 월요일인 경우 경고 메시지를 출력하라.
# 입력이 완료되면 연, 월, 날짜, 그리고 요일을 dictionary에 정리하여 출력하라.
# HINT: calendar 모듈을 활용하라.	(공식문서 링크)

# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar

year = int(input())
while(calendar.isleap(year)):
    print('윤년입니다. 연도를 다시 입력해주세요')
    year = int(input())

print(calendar.TextCalendar().formatyear(year))
month = int(input())
day = int(input())

weekday_num = calendar.weekday(year, month, day)
weekday_kor = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}
weekday = weekday_kor[weekday_num]

date = {'년': 0, '월': 0, '일':0, '요일': ''}
date['년'] = year
date['월'] = month
date['일'] = day
date['요일'] = weekday + '요일'

if weekday == '월':
    print('경고 월요일입니다.')

print(date)