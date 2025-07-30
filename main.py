class item:
    pay_rate=0.8
    def __init__(self,name:str,price:int,quantity=0):
        assert price>=0,f"the price {price} must be greater or equal to zero"
        assert quantity>=0,f"the quantity  {quantity} must be greater or equal to zero"
        
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def calculate_total_price(self):
        return self.quantity*self.price
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate
        
    
item1=item("phone",100,2)
item1.apply_discount()
print(item1.price)


item2=item("laptop",1000,4)
item2.pay_rate=0.7
item2.apply_discount()
print(item2.price)

print(item.__dict__) #all atributes for class lavel
print(item1.__dict__)#all atributes for instance  lavel