import csv

class Item:

    #class attributes
    disc_per=0.4
    all=[]

    #constructor and simple method
    def __init__(self,name:str,price:float,quantity:int):

        # Run Validation on Received Arguments
        assert price>0,'price must be greated then 0'
        assert quantity>0,'Quantity must be greater then 0'

        #Assign Values to Instance Variablea
        self.__name=name
        self.price=price
        self.quantity=quantity

        #Actions to Execute

        Item.all.append(self)

    def calculateTotalPrice(self):
        return self.price*self.quantity

    def applyDiscount(self):
        self.price=self.price*Item.disc_per


    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,value):
        self.__name==value


    @classmethod
    def instantiateFromCsv(cls):
        with open('items.csv','r') as file:
            reader=csv.DictReader(file)
            items=list(reader)
        # print(items)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    #magic / dunder methods methods
    def __repr__(self):
        return f"{self.name} {self.price} {self.quantity}"

Item.instantiateFromCsv()


# soap=Item('soap',40,2)
# shampoo=Item('shampoo',40,2)
# conditioner=Item('conditioner',40,2)
# facewash=Item('facewash',40,2)
# print('this is a price')
# soap.applyDiscount()
# print(soap.calculateTotalPrice())
#
print(Item.all)