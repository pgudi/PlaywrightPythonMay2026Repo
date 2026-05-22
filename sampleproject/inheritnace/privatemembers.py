class Bank:
    def __init__(self):
        self.__bankname="HDFC Bank"
        self.__accountno=10000011
        
class Loan(Bank):
    pass

obj=Loan()
print(obj.__bankname)
print(obj.__accountno)
