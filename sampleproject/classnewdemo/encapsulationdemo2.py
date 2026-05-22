class Bank:
    def __init__(self,bname,acc):
        self.__bankname=bname
        self.__accountNumber=acc

    def get_bank_name(self):
        return self.__bankname

    def get_account_number(self):
        return self.__accountNumber

obj=Bank("Axis Bank",10000011)
print(obj.get_bank_name())
print(obj.get_account_number())