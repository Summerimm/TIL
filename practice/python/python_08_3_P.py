# 문제
# 아래의 명세를 읽고 Python 클래스를 활용하여 PublicTransport을 표현하시오.
# A. PublicTransport는 이름 name 과 요금 fare을 인스턴스 속성으로 가진다.
# B. 탑승get_in, 하차get_off하는 메서드를 필요로 한다.    
#   i. 이 때, passenger의 수를 받는다.
# C. 현재 탑승자 수를 알 수 있어야 한다.
# D. 최종 수익을 계산하는 메소드 profit 은 요금과 전체 탑승자 수를 곱해서 계산한다. 

class PublicTransport:
    passenger = 0

    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
    
    def get_in(self, num):
        self.passenger += num
        return self.passenger

    def get_off(self, num):
        self.passenger -= num
        return self.passenger

    def profit(self):
        cost = self.fare * self.passenger
        return cost

p1 = PublicTransport('지하철', 12)
print(p1.get_in(10))
print(p1.get_off(5))
print(p1.profit())

p2 = PublicTransport('버스', 8)
print(p2.get_in(19))
print(p2.get_off(3))
print(p2.get_in(6))
print(p2.profit())