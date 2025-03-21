#first_day
#  class Car:
#     def __init__(self , brand, model , year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"汽車資訊: {self.brand}的{self.model}年分{self.year}")

#     def start_engine(self):
#         print(f"{self.brand}的{self.model}發動了!!")


# car1 = Car("Toyota", "Corolla", 2023)
# car2 = Car("Tesla", "Model S", 2024)


# car1.display_info()
# print("\n")
# car1.start_engine()
# print("\n")
# car2.display_info()
# print("\n")
# car2.start_engine()
#====================================================
# 第二天：Python OOP - 繼承（Inheritance）與多型（Polymorphism）

#建立父類別

class Vehicle:
    def __init__(self, brand,year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"這是一台{self.year}的{self.brand}交通工具")

#建立子類別
class Car(Vehicle):
    def __init__(self, brand,year,fuel_type): # 初始化汽車
        super().__init__(brand, year)#  使用 super() 繼承父類別的屬性
        self.fuel_type = fuel_type#  新增子類別的獨有屬性

    def display_info(self): #覆寫 display_info 方法
        print(f"這是一台 {self.year} 年的 {self.brand} 汽車，使用 {self.fuel_type} 作為燃料")


class Bike(Vehicle):
    def __init__(self, brand, year,bike_type): # 初始化腳踏車
        super().__init__(brand, year) #使用 super() 繼承父類別的屬性
        self.bike_type = bike_type #新增子類別的獨有屬性

    def display_info(self): #覆寫 display_info 方法
        print(f"這是一台 {self.year} 年的 {self.brand} 腳踏車，類型為 {self.bike_type}")

vehicles = [
    Car("Toyota", 2023, "Gasoline"),
    Bike("Giant", 2021, "Mountain")
]
#迴圈遍歷 vehicles，並呼叫 display_info()（多型的應用:同樣的方法在不同類別的物件上表現出不同的行為）
for v in vehicles:
    v.display_info()
        

print("dev_branch test")