class Bank:
    def __init__(self):
        self.__bankname=""
        self.__accountNumber=0

    def set_bank_name(self, bankname):
        self.__bankname=bankname

    def set_account_number(self, accnumber):
        self.__accountNumber=accnumber

    def get_bank_name(self):
        return self.__bankname

    def get_account_number(self):
        return self.__accountNumber

obj=Bank()

obj.set_bank_name("ICICI Bank")
obj.set_account_number(10000011)
print(obj.get_bank_name())
print(obj.get_account_number())