class Fruit:
    def __init__(self, name, color, texture, price):
        self.name = name
        self.color = color
        self.texture = texture
        self.price = float(price)

#prints fruit details 
    def details(self):
        print(f"""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Fruit Type: {self.name}
            Fruit Color: {self.color}
            Fruit Texture: {self.texture}
            Fruit Cost: {self.price}
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)
    def calc_sales_tax(self, tax):
        total = (self.price*tax) + self.price
        print(f"""
        *********************************************
            Total Cost of {self.name}: {total}
        *********************************************
            """)

apple = Fruit("apple", "red", "smooth", 1.25)
pear = Fruit("pear", "green", "soft", 1.50)
strawberry = Fruit("strawberry", "red", "seedy", 3.25)
orange = Fruit("orange", "orange", "waxy", 1.75)

apple.details()
pear.details()
strawberry.details()
orange.details()

apple.calc_sales_tax(.04)
pear.calc_sales_tax(.04)
strawberry.calc_sales_tax(.04)
orange.calc_sales_tax(.04)