# GitHub Link -> https://github.com/edyoda/DS-Assignments/blob/main/Final_Project.md

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock


class Admin:
    food_items = []
    next_food_id = 1

    @classmethod
    def add_food_item(cls, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = cls.next_food_id
        cls.next_food_id += 1
        cls.food_items.append(food_item)

    @classmethod
    def edit_food_item(cls, food_id, name, quantity, price, discount, stock):
        for item in cls.food_items:
            if item.food_id == food_id:
                item.name = name
                item.quantity = quantity
                item.price = price
                item.discount = discount
                item.stock = stock
                break

    @classmethod
    def view_food_items(cls):
        for item in cls.food_items:
            print(
                f"FoodID: {item.food_id}, Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}, Discount: {item.discount}, Stock: {item.stock}")

    @classmethod
    def remove_food_item(cls, food_id):
        cls.food_items = [
            item for item in cls.food_items if item.food_id != food_id]


class User:
    users = []
    next_user_id = 1

    def __init__(self, full_name, phone_number, email, address, password):
        self.user_id = User.next_user_id
        User.next_user_id += 1
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    @classmethod
    def register(cls, full_name, phone_number, email, address, password):
        user = cls(full_name, phone_number, email, address, password)
        cls.users.append(user)
        return user

    @classmethod
    def login(cls, email, password):
        for user in cls.users:
            if user.email == email and user.password == password:
                return user

    def place_order(self, food_ids):
        order_items = []
        total_price = 0

        for food_id in food_ids:
            for item in Admin.food_items:
                if item.food_id == food_id:
                    order_items.append(item)
                    total_price += item.price

        self.orders.append((order_items, total_price))
        return total_price

    def view_order_history(self):
        for i, (items, total_price) in enumerate(self.orders):
            print(f"Order {i+1}:")
            for item in items:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")
            print(f"Total Price: INR {total_price}\n")

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password


# Example usage:
Admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 50)
Admin.add_food_item("Vegan Burger", "1 piece", 320, 10, 30)
Admin.add_food_item("Truffle Cake", "500gm", 900, 15, 20)

Admin.view_food_items()

Admin.remove_food_item(2)

Admin.view_food_items()

user1 = User.register("abc", "123456789",
                      "sdfg@sdfgh.gfd", "sdfghtfdxtgh sdsfcghj 3456", "qwertyuiop")

user1.place_order([1, 3])
user1.view_order_history()

user1.update_profile("try", "987654321",
                     "zxcv@zxc.com", "234 dfgh lkj", "mnbvcxz")
