class item:
    all=[]
    pay_rate=0.8
    def __init__(self,name:str,price:int,quantity=0):
        assert price>=0,f"the price {price} must be greater or equal to zero"
        assert quantity>=0,f"the quantity  {quantity} must be greater or equal to zero"
        
        self.name=name
        self.price=price
        self.quantity=quantity
        item.all.append(self)
    def calculate_total_price(self):
        return self.quantity*self.price
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate
    # it prints items isted of their instances or location
    def __repr__(self):
        return f"item('{self.name}','{self.price},'{self.quantity}')"
        
item1 = item("Phone", 100, 1)
item2 = item("Laptop", 1000, 3)
item3 = item("Cable", 10, 5)
item4 = item("Mouse", 50, 5)
item5 = item("Keyboard", 75, 5)
print(item.all)

# for instance in item.all:
#     print(instance.name)

# print(item.__dict__) #all atributes for class lavel
# print(item1.__dict__)#all atributes for instance  lavel