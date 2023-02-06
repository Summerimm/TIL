# 문제
# 코딩테스트 온라인 감독을 하는 중이다. 다음과 같은 딕셔너리를 줬을 때 다음의 요구사항을 수행하라.

# dictionary의 value로 solving, sleeping, cheating이 있다.
# 커닝하고 있는 사람의 상태는 cheating이다.
# 커닝하고 있는 사람을 시험장에서 퇴출해야 한다. test_status에서 상태가 cheating인 요소를 제거하라.
# 커닝을 하고 있는 사람의 리스트를 오름차순으로 출력하라.

# 잠을 자고 있는 사람의 상태는 sleeping이다.
# 잠을 자고 있는 사람을 깨워야 한다. test_status에서 안의 모든 sleeping을 solving으로 바꿔라.
# 위의 모든 요구사항을 수행한 뒤 test_status를 출력하라.

# 출력 예시
# ['염자바', '임온실', '최이썬']
# test_status = {'김코딩': 'solving', '이싸피': 'solving', '오디비': 'solving',
# 		'조실습': 'solving', '박장고': 'solving'}

test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

cheat_list = []

for name, stat in test_status.items():
	if stat == 'sleeping':
		test_status[name] = 'solving'
	if stat == 'cheating':
		cheat_list.append(name)

for name in cheat_list:
	del test_status[name]

cheat_list.sort()

print(cheat_list)
print(test_status)


