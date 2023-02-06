# 문제
# 아래의 명세를 읽고 Python 클래스를 활용하여 사람(Person)을 표현하시오.
# 1. 사람은 이름과 나이를 가진다.
# 2. 사람을 인스턴스를 생성하는 방법은 2가지다.   
#   A. 생성자       
#       i. 이름과 나이를 인자로 받는다.   
#   B. get_age 클래스 메서드       
#       i. 이름과 태어난 연도를 받아 나이로 변환하고, 새로운 Person 객체를 반환한다.
# 3. 인스턴스의 나이를 확인하는 메서드 check_age를 만든다.   
#   A. 미성년자의 기준을 미성년자 여부를 True, False로 반환한다. 미성년자는 19세를 기준으로 한다.

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    @classmethod
    def get_age(cls, name, year):
        cls.name = name
        cls.age = 2023 - year + 1
        return Person(cls.name, cls.age)
    
    def check_age(self):
        if self.age <= 19:
            return True
        else:
            return False

#Driver's code
person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age) 
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())
