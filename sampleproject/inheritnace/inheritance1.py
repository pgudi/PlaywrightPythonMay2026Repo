class Product:
    
    def show_quantity(self, quantity):
        print("Quantity :"+quantity)

    def show_prod_name(self, prodname):
        print("Product Name :",prodname)

    def show_prod_price(self,price):
        print("Prodct Price :",price)

class Customer(Product):
    def show_customer_name(self,cname):
        print("Customer Name :",cname)

obj=Customer()
obj.show_customer_name("S G Institute")
obj.show_prod_name("Dell Desktop")
obj.show_prod_price(37000)
obj.show_quantity("10 Laptops")