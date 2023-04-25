import Beverage as B
import Storage
from Storage import Material as m
from Beverage import menu


class BeverageFactory():
    def __init__(self, name, size,ice,sweet):
        drink = menu[name]
        if size == "大杯": 
            self.price=drink.bigprice
            self.size = 2
        elif size == "中杯":
            self.price = drink.price
            self.size = 1
        
        self.ice = ice
        self.sweet =sweet
        self.source = []
        for key in drink.source.keys():
            self.source.append(m(key,self.size))
        
    def addtoppings(self,*a):
        li = a[0]
        for i in li:
            st = str(i[1:])
            if i[0] == '加':
                self.source.append(m(st,1))
                self.price+=Storage.Storage().pricestock[self.source[-1].name] 
            elif i[0] == '去':
                for j in self.source:
                    if j.name == st:
                        self.source.remove(j)
                        del j

       
        


