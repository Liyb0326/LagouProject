class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describle_restaurant(self):
        print(f"restaurant name is {self.restaurant_name}")
        print(f"cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print("餐厅正在营业。。。")

    def set_number_served(self,numberserve):
        self.number_served=numberserve

    def increment_number_served(self, numberserve):
        self.number_served += numberserve


res1 = Restaurant('whikk','west')

res1.increment_number_served(10)
res1.increment_number_served(20)

print(res1.number_served)
