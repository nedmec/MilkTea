import Storage

class Beverage:
    def __init__(self, name, ice, sweet, *args,**kwargs):
        self.name = name
        self.ice = ice
        self.sweet = sweet
        self.source = args[0]
        self.price = 0
        for key in args[0].keys():
            self.price += Storage.Storage.pricestock[key]
        self.bigprice = round(self.price*1.5)
        
    def __del__(self):
        for i in self.source:
            del i
menu = {
    "奶茶类------------------":0,
    "珍珠奶茶":Beverage("珍珠奶茶",0,0,{"牛奶":1,"绿茶":1,"珍珠":1}),
    "椰果奶茶":Beverage("椰果奶茶",1,0,{"牛奶":1,"绿茶":1,"椰果":1}),
    "果茶类------------------":0,
    "柠檬绿茶":Beverage("柠檬绿茶",0,0,{"绿茶":1}),
}


