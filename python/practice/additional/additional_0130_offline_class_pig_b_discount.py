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
        
    def order_original_price(self, amount):
        if self.stock >= amount:
            return self.original_price() * amount
            # return Pig.belly_price * amount

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

    # b 돼지의 가격이 20% 할인됨
    def discount(self, percentage):
        self.belly_price = int(self.belly_price * (1 - percentage))
        return self.belly_price

    # b 돼지에서 원래 가격도 접근 가능함
    # def original_price(self):
    #     return Pig.belly_price

    @classmethod
    def original_price(cls):
        return cls.belly_price

    def both_price(self, amount):
        return self.order_price(amount), self.order_original_price(amount)

a_pig = Pig(100)
b_pig = Pig(150)

# b 돼지의 가격이 20% 할인됨
# b_pig.belly_price = b_pig.belly_price*(1-0.2)
b_pig.discount(0.2)
print(b_pig.belly_price)

# b 돼지에서 원래 가격도 접근 가능함
print(b_pig.original_price())

# b 돼지를 50만큼 샀을 때, 원래 가격, 할인된 가격 둘다 반환.
# print(b_pig.order_price(50))
# print(b_pig.order_original_price(50))
print(b_pig.both_price(50))