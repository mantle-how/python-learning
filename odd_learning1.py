class Car:
    def __init__(self , brand, model , year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"汽車資訊: {self.brand}的{self.model}年分{self.year}")

    def start_engine(self):
        print(f"{self.brand}的{self.model}發動了!!")


car1 = Car("Toyota", "Corolla", 2023)
car2 = Car("Tesla", "Model S", 2024)


car1.display_info()
print("\n")
car1.start_engine()
print("\n")
car2.display_info()
print("\n")
car2.start_engine()
