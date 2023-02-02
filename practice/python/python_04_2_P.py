# 문제
# 1.   주어진 리스트는 반장선거 투표 결과이다. 득표가 많은 순서대로 출력하시오. 단, 딕셔너리를 사용할 것이며, 외부 패키지는 사용하지 않는다.

students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이', '강디티']
vote_dict = {}

for idx, student in enumerate(students):
    if student not in vote_dict.keys():
        vote_dict[student] = 1
    else:
        vote_dict[student] += 1

print(vote_dict)