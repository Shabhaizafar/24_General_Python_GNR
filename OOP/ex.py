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

# ///////////////////////////.
'''
-> Problem Statement: Multi-tiered E-commerce System with Dynamic Pricing

Background:
You are developing a backend system for a large e-commerce platform that sells various types of products, including electronics, clothing, groceries, and digital goods. The platform supports multiple user tiers (such as regular users, premium users, and affiliate users), each with different pricing and discount strategies. The platform also supports a variety of product categories, each with specific behaviors when it comes to pricing adjustments, seasonal discounts, and special promotions.

You need to implement a polymorphic structure that handles different pricing strategies for various user tiers, product categories, and types of discounts. You also need to ensure that the system is flexible enough to easily add new pricing rules in the future without significantly altering existing code.

- Requirements:
1. User Tier-based Pricing:
   - Regular users receive a base price with no discounts.
   - Premium users receive a 10% discount on all products.
   - Affiliate users receive a 15% discount on electronics and digital goods, and 5% on clothing and groceries.

2. Product Category-based Pricing:
   - Electronics: Discounts for affiliate users based on price thresholds.
   - Clothing: Seasonal discounts, e.g., 20% off during sales periods.
   - Groceries: Discounts based on weight or volume, e.g., "Buy 2, get 1 free" offers.

3. Dynamic Pricing:
   - During high demand (e.g., holidays or special events), prices may surge for specific product categories like electronics.
   - For digital goods, there could be a time-sensitive discount that expires after a certain date.

4. Polymorphic Classes:
   - You will use polymorphism to implement the dynamic pricing system, where different strategies for pricing calculations (based on user tier, product category, and time-sensitive rules) are handled via subclasses of a generic `Product` class and a `User` class.
   
5. Extensibility:
   - The system should allow new pricing rules to be added easily in the future without modifying existing class methods too much.

- Specific Tasks:
- Create the base `Product` class with common attributes like `name`, `category`, and `price`.
- Create subclasses for different product categories (e.g., `Electronics`, `Clothing`, `Groceries`), each with a method to calculate the final price based on specific category rules.
- Create a base `User` class and subclasses for each user tier (e.g., `RegularUser`, `PremiumUser`, `AffiliateUser`), each with a method to apply discounts based on the user type.
- Implement dynamic pricing adjustments for special conditions (e.g., surge pricing or time-sensitive discounts).
- Ensure that the final price is calculated correctly by using polymorphism to call different methods for product category and user tier, and allow for easy updates or new rules.

- Example Flow:

- A `PremiumUser` wants to buy an `Electronics` product priced at $100.
  - The `PremiumUser` class applies a 10% discount.
  - The `Electronics` class checks if there is a time-sensitive promotion (e.g., a 5% discount) and applies it.
  - The final price is calculated dynamically.

- An `AffiliateUser` wants to buy a `Clothing` item priced at $50.
  - The `AffiliateUser` class applies a 5% discount for clothing items.
  - The `Clothing` class checks if a seasonal discount (e.g., 20% off) applies.
  - The final price is dynamically computed considering both discounts.
'''
