# 문제
# add, subtract, multiply, divide 메소드를 가진 Calculator 클래스를 생성하고, 아래의 계산 결과를 출력하라. 
#  단, 숫자는 0으로 나눌 수 없다. 이 경우, 예외처리로 0으로 나눌 수 없습니다.를 출력하라. 

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        try:
            return self.a / self.b
        except ZeroDivisionError as err:
            return f'{err}: 0으로 나눌 수 없습니다'
# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0
print(Calculator(1, 2).add())
print(Calculator(2, 1).subtract())
print(Calculator(3, 4).multiply())
print(Calculator(4, 0).divide())