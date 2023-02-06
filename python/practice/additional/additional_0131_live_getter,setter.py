class Person:
    def __init__(self) -> None:
        self._age = 0
    
    @property
    def age(self): # getter
        print('call getter')
        return self._age
        
    @age.setter
    def age(self, age): # setter
        print('call setter')
        self._age = age


#p1 = Person()
# p1._age = 25 -> 가능, but 암묵적으로 쓰면 안 됨
# print(p1._age) -> 가능, but 암묵적으로 쓰면 안 됨 

# # 불편한 방법
# p1.set_age(25)
# print(p1.get_age())

p1 = Person()
p1.age = 25
print(p1.age)