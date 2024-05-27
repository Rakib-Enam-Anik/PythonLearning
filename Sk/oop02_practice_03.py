class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, odr2):
        return self.price > odr2.price
    
ordr1 = Order("Chips", 20)
odr2 = Order("tem", 15)

print(ordr1 > odr2)