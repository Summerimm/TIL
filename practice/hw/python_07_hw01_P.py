# 문제
# 개의 속성과 행위를 정의하는 Doggy 클래스를 만들어라.

# 구성 요소    
# i. 초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.    
# ii. bark() 메서드를 호출하면 개는 짖을 수 있다.    
# iii. 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다. 
#       개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다.                       
#       개가 죽으면 num_of_dogs의 값이 1 감소한다.    
# iv. get_status() 메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다 

class Doggy:
    birth_of_dogs = 0 # 클래스 변수
    num_of_dogs = 0
    
    def __init__(self, name, breed):
        self.name = name # 인스턴스 변수
        self.breed = breed
        self.num_of_dogs += 1

    def bark(self):
        return '멍멍'

    def birth(self):
        self.birth_of_dogs += 1
        self.num_of_dogs += 1
    
    def death(self):
        self.num_of_dogs -= 1

    def get_status(self):
        return f'birth_of_dogs: {self.birth_of_dogs}, num_of_dogs: {self.num_of_dogs}'

dog1 = Doggy('아롱이', '닥스훈트')
dog2 = Doggy('초롱이', '비글')
dog3 = Doggy('닐라', '리트리버')
dog3.birth()
dog2.death()
print(dog1.name)
print(dog2.breed)
print(dog1.bark())
print(dog3.get_status())