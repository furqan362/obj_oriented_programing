import csv
class Item:
    
    
    all=[]
    pay_rate=0.8
    def __init__(self,name:str,price:int,quantity=0):
        assert price>=0,f"the price {price} is not greater or equal to zero"
        assert quantity>=0,f"the quantity  {quantity} is not greater or equal to zero"
        #  by underscore we dont access it from instance lavel
        self.__name=name
        self.__price=price
        self.quantity=quantity
        Item.all.append(self)
    
    # property deceroter read only attributes
    @property
    def name(self):
        return self.__name
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate
    
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    def price(self):
        return self.__price

    #  it allows user to change name 
    @name.setter
    def name(self,value):
        if len(value)>10:
            raise Exception ("your name is too long")
        else:
            self.__name=value
    
    def calculate_total_price(self):
        return self.quantity*self.price
    
    
        
    
    
    
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

    @staticmethod
    def is_integer(num):
            # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
# it prints items insted of their instances or location
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"