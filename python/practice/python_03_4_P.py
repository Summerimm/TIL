# 문제
# 1. 여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 만드시오.

blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
blood_dict = {'A': 0, 'B': 0, 'O':0, 'AB': 0}

for data in blood_types:    
    blood_dict[data] += 1

print(blood_dict)