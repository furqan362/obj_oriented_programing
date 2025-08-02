from item import Item

class phone(Item):
    all=[]
    def __init__(self, name, price, quantity=0,broken_phones=0):
        # call super function to access all atributes of our parent class
        super().__init__(name, price, quantity)
        # assert broken phones  
        assert broken_phones>=0,f"the broken_phones  {broken_phones} is not greater or equal to zero"
        # assing to self object
        self.broken_phones=broken_phones
        phone.all.append(self)
        phone1=phone("iphone9",1000,4,1)
