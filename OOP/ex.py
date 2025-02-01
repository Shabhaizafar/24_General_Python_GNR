class FoodItem:
    def get_price(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Appetizer(FoodItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
class MainCourse(FoodItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
class Dessert(FoodItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price

class Order:
    def __init__(self):
        self.items = []
    def add_item(self, item: FoodItem):
        self.items.append(item)
    def calculate_total(self):
        total = sum(item.get_price() for item in self.items)
        return total
# Creating food items
appetizer1 = Appetizer("Gota", 20)
main_course1 = MainCourse("Pav Bhaji", 100)
dessert1 = Dessert("Ice cream", 20)
# Creating an order
order = Order()
order.add_item(appetizer1)
order.add_item(main_course1)
order.add_item(dessert1)
# Calculating the total price of the order
total_price = order.calculate_total()
print(f"Total Price: Rs.{total_price:.2f}")