class Storage:
    stock = {
        "牛奶": 5,
        "珍珠": 100,
        "椰汁": 50,
        "草莓": 30,
        "哈密瓜": 20,
        "西瓜": 200,
        "椰果": 200,
        "蓝莓": 200,
        "芒果": 50,
        "山楂": 50,
        "桑葚": 50,
        "铁观音": 100,
        "龙井": 50,
        "茉莉花茶": 50,
        "桂花茶": 50,
        "柠檬茶": 30,
        "绿茶": 30,
        "红茶": 30,
        "荔枝茶": 50,
        "葡萄": 100,
        "苹果": 50,
        "桂花": 30,
 
}
    pricestock = {
        "牛奶": 5,
        "珍珠": 10,
        "椰汁": 5,
        "草莓": 3,
        "哈密瓜": 2,
        "西瓜": 20,
        "椰果": 2,
        "蓝莓": 20,
        "芒果": 5,
        "山楂": 5,
        "桑葚": 5,
        "铁观音": 10,
        "龙井": 5,
        "茉莉花茶": 5,
        "桂花茶": 5,
        "柠檬茶": 3,
        "绿茶": 3,
        "红茶": 3,
        "荔枝茶": 5,
        "葡萄": 10,
        "苹果": 5,
        "桂花": 3,

    }
    def get_ingredient(self, ingredient_name, num):
        num = int(num)
        self.stock[ingredient_name] -= num
        if ingredient_name not in self.stock:
            return ingredient_name+"不存在"
        if self.stock[ingredient_name] <= num:
            return ingredient_name+"原料不足"
        
        return ""
    
    def return_ingredient(self, ingredient_name, num):
        num = int(num)
        self.stock[ingredient_name] += num


class Material(Storage):
    def __init__(self, name, num):
        self.errormesssage = Storage.get_ingredient(self, name, num)
        self.name = name
        self.num = num

    def __del__(self):
        Storage().return_ingredient(self.name, self.num)