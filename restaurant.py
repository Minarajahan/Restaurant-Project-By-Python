# restaurant.py

class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.item_id}. {self.name} - ${self.price:.2f}"


class Menu:
    def __init__(self):
        self.items = []

    def load_menu(self):
        try:
            with open("menu.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        item = MenuItem(int(parts[0]), parts[1], float(parts[2]))
                        self.items.append(item)
        except FileNotFoundError:
            print("Menu file not found. Starting with an empty menu.")

    def display_menu(self):
        print("\n--- MENU ---")
        for item in self.items:
            print(item)

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None


# ✅ Add these classes below the Menu class — for ordering

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def get_total_price(self):
        return self.menu_item.price * self.quantity

    def __str__(self):
        return f"{self.menu_item.name} x{self.quantity} = ${self.get_total_price():.2f}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity):
        self.items.append(OrderItem(menu_item, quantity))

    def display_order(self):
        print("\n--- ORDER SUMMARY ---")
        total = 0
        for item in self.items:
            print(item)
            total += item.get_total_price()
        print(f"\nTotal Bill: ${total:.2f}")
