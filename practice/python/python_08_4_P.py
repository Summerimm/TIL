# 문제
# 아래의 명세를 읽고 Python 클래스를 활용하여 PublicTransport을 표현하시오.
# A. PublicTransport는 이름 name 과 요금 fare을 인스턴스 속성으로 가진다.
# B. 탑승get_in, 하차get_off하는 메서드를 필요로 한다.    
#   i. 이 때, passenger의 수를 받는다.
# C. 현재 탑승자 수를 알 수 있어야 한다.
# D. 최종 수익을 계산하는 메소드 profit 은 요금과 전체 탑승자 수를 곱해서 계산한다. 

# 문제
# 앞서 제작한 PublicTransport의 subclass Bus 클래스를 만들어라.
# A. 탈 수 있는 인원을 제한하기 위한 인스턴스 변수를 추가해라.
# B. get_in 메서드를 오버라이딩하여 탈 수 있는 인원보다 많은 인원이 탑승하려고 한다면 더이상 탑승할 수 없습니다. 라는 문구를 출력하고 종료하라. 

class PublicTransport:
    passenger = 0

    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
    
    def get_in(self, num):
        self.passenger += num
        return f'현재 승객 수: {self.passenger}'

    def get_off(self, num):
        self.passenger -= num
        return f'현재 승객 수: {self.passenger}'

    def profit(self):
        cost = self.fare * self.passenger
        return f'수익: {cost}'

class Bus(PublicTransport):
    def __init__(self, name, fare, limit):
        super().__init__(name, fare)
        self.limit = limit

    def get_in(self, num):
        if self.passenger + num > self.limit:
            return '더 이상 탑승할 수 없습니다.'
        else:
            self.passenger += num
            return f'현재 승객 수: {self.passenger}'


p1 = PublicTransport('지하철', 12)
print(p1.get_in(10))
print(p1.get_off(4))
print(p1.profit())

p2 = Bus('버스', 8, 10)
print(p2.get_in(7))
print(p2.get_off(3))
print(p2.get_in(7))
print(p2.profit())