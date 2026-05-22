class Product:
    productName="Lenovo Laptop"

    @classmethod
    def change_product_name(cls,newname):
        cls.productName=newname
        print("New Product Name :",cls.productName)


print(Product.productName)
Product.change_product_name("Dell Desktop")

