# 11.1-11.3

def z111():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
    print(f"Тип кухни: {self.cuisine_type}")
    def open_restaurant(self):
        print("Ресторан открыт!")
    new_restaurant = Restaurant("Pizza Planet", "итальянская")
    print(new_restaurant.restaurant_name)
    print(new_restaurant.cuisine_type)
    new_restaurant.describe_restaurant()
    new_restaurant.open_restaurant()

def z112():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
    print(f"Тип кухни: {self.cuisine_type}")
    restaurant1 = Restaurant("McDonald's", "фастфуд")
    restaurant2 = Restaurant("KFC", "фастфуд")
    restaurant3 = Restaurant("Subway", "фастфуд")
    restaurant1.describe_restaurant()
    print()
    restaurant2.describe_restaurant()
    print()
    restaurant3.describe_restaurant()

def z113():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.rating = rating
    def describe_restaurant(self):
print(f"Название ресторана: {self.restaurant_name}")
print(f"Тип кухни: {self.cuisine_type}")
print(f"Рейтинг: {self.rating}")
    def update_rating(self, new_rating):
    self.rating = new_rating
    restaurant1 = Restaurant("McDonald's", "фастфуд")
    restaurant2 = Restaurant("KFC", "фастфуд")
    restaurant3 = Restaurant("Subway", "фастфуд", rating=4)
    restaurant1.describe_restaurant()
    print()
    restaurant2.describe_restaurant()
    print()
    restaurant3.describe_restaurant()
    print()
    restaurant1.update_rating(3)
    restaurant2.update_rating(2)
    restaurant3.update_rating(5)
restaurant1.update_rating(3)
restaurant2.update_rating(2)
restaurant3.update_rating(5)
restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()