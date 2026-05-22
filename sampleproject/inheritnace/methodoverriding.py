class CaptialCity:
    def dsiplay_cityname(self, cityname):
        print("The Capital City name :",cityname)

class Metropolitian(CaptialCity):
    def __init__(self, cityname):
        super().dsiplay_cityname(cityname)

    def dsiplay_cityname(self, cityname):
        print("The Metropolitian City name :",cityname)

obj1=Metropolitian("Bangalore")
obj1.dsiplay_cityname("Mumbai")
