class Pig:
    belly_price = 1000 # 클래스 변수

    def __init__(self, stock):
        self.stock = stock

    # 주문이 들어왔을 때의 가격 -> 메서드
    def order_price(self, amount):
        if self.stock >= amount:
            return self.belly_price * amount

        else:
            return "재고가 없어요."
            # return f"재고가 {self.stock}만큼 있습니다"
        

    def order(self, amount, money):
        
        price = self.order_price(amount)
        if price <= money:
            self.stock = self.stock - amount
            change = money - price
            return change
        else: 
            return '못삼'
        
    @classmethod
    def func(cls, amount, percentage):
        origin_price = cls.belly_price * amount
        discount_price = origin_price * (1 - percentage)
        return f'원래 가격: {origin_price}, 할인된 가격: {discount_price}'

    def discount(self, percentage):
        self.belly_price = self.belly_price * ( 1 - percentage)
        return self.belly_price

a_pig = Pig(100) # 인스턴스 생성
b_pig = Pig(150) # 인스턴스 생성
# print(a_pig.belly_price) # 1000
# print(b_pig.belly_price) # 1000

b_pig.belly_price = 500 # 클래스 변수 변경
# print(a_pig.belly_price) # 1000
# print(b_pig.belly_price) # 500

# print(a_pig.stock) # 100
# print(a_pig.order(50, 10000000)) # 거스름돈 9950000
# print(a_pig.stock) # 100 - 50 = 50
# print(b_pig.stock) # 150
# print(a_pig.order_price(150)) # 재고가 없어요

#-------------------------------------------------------
# b 돼지의 가격이 20% 할인됨
# b 돼지에서 원래 가격도 접근 가능함
# b 돼지를 50만큼 샀을 때, 원래 가격, 할인된 가격 둘다 반환.
print(b_pig.func(50, 0.2))