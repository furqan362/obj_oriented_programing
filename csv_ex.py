import csv

class Item:
    all=[]
    pay_rate=0.8
    def __init__(self,name:str,price:int,quantity=0):
        assert price>=0,f"the price {price} must be greater or equal to zero"
        assert quantity>=0,f"the quantity  {quantity} must be greater or equal to zero"
        
        self.name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.quantity*self.price
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate
        
    # it prints items isted of their instances or location
    def __repr__(self):
        return f"item('{self.name}','{self.price},'{self.quantity}')"
    
    @classmethod
    def instance_from_csv(cls):
        with open('item.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
Item.instance_from_csv()
print(Item.all)