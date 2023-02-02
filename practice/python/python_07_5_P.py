# 페어 프로그래밍은 하나의 컴퓨터에서 두 사람의 프로그래머가 작업하는 방식을 의미한다.
# 진정한 프로그래머가 되기 위해 김해피는 페어를 매칭하기 위한 프로그램을 작성하려고 한다. 
# 클래스를 활용해 작성하며 포함되는 메서드는 아래와 같다.

# i. 초기화 메서드는 인자로 학생 이름으로 구성된 리스트를 받아서 인스턴스 변수에 할당한다.
# ii. pick(n) 메서드는 학생들 명단에서 인자 n명 만큼 랜덤으로 추출하여 return한다.
# iii. match_pair() 메서드는 학생들 명단을 랜덤으로 2명씩 매칭해 준다. 이때, 학생들 명단의 수가 홀수명이면 단 한팀만 3명으로 구성한다.     

import random

class ClassHelper:
    def __init__(self, datalist) -> None:
        self.datalist = datalist
    
    def pick(self, num):
        return random.sample(self.datalist, num)

    def match_pair(self):
        random.shuffle(self.datalist) # 학생 섞기
        anslist = [] # 그룹핑 넣을 리스트
        for i in range(len(self.datalist) // 2): 
            anslist.append(self.datalist[2*i:2*i+2]) # 섞인 학생 명단 2명씩 자르기
        if len(self.datalist) % 2 == 1: # 학생 수가 홀수
            anslist[-1].append(self.datalist[-1])
        return anslist

ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
