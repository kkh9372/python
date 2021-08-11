# 자동차 클래스 정의
class Car:
    def __init__(self, model, color, price):
        # 속성
        self.model  = model
        self.color  = color
        self.price  = price

    # 기능
    def speedUP(self):
        print('%s speed Up...' % self.model)
    def speedDown(self):
        print('%s speed Down...' % self.model)
    def show(self):
        print('차량명 :', self.model)
        print('차량색 :', self.color)
        print('차량가격 :', self.price)