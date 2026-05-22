class Payment:
    def pay(self):
        print("Payment process has started")

class PhonePe(Payment):
    def pay(self):
        print("Payment process has started by using PhonePe")

class GooglePay(Payment):
    def pay(self):
        print("Payment process has started by using GooglePay")

class NetBanking(Payment):
    def pay(self):
        print("Payment process has started by using NetBanking")

obj=Payment()
obj.pay()

obj=PhonePe()
obj.pay()

obj=GooglePay()
obj.pay()

obj=NetBanking()
obj.pay()