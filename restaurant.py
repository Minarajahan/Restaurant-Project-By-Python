# restaurant.py

class MenuItem:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = []

    def load_menu(self):
        self.items = [
            MenuItem(1, "Burger", 5.99),
            MenuItem(2, "Pizza", 7.99),
            MenuItem(3, "Coffee", 2.50),
            MenuItem(4, "Salad", 4.75)
        ]

    def display_menu(self):
        print("Menu:")
        for item in self.items:
            print(f"{item.id}. {item.name} - ${item.price}")

    def get_item_by_id(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def get_total_price(self):
        return self.menu_item.price * self.quantity

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity):
        self.items.append(OrderItem(menu_item, quantity))

    def display_order(self):
        print("\nYour Order:")
        for item in self.items:
            print(f"{item.menu_item.name} x{item.quantity} = ${item.get_total_price():.2f}")
        total = sum(item.get_total_price() for item in self.items)
        print(f"Total: ${total:.2f}")

    def save_order_to_file(self, customer_name):
        with open("orders.txt", "a") as file:
            file.write(f"Order by {customer_name}:\n")
            for item in self.items:
                file.write(f"{item.menu_item.name} x{item.quantity} = ${item.get_total_price():.2f}\n")
            total = sum(item.get_total_price() for item in self.items)
            file.write(f"Total: ${total:.2f}\n")
            file.write("-------------------------\n")

    def print_bill(self, customer_name):
        from datetime import datetime
        total = sum(item.get_total_price() for item in self.items)
        filename = f"bill_{customer_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as file:
            file.write("=== RESTAURANT BILL ===\n")
            file.write(f"Customer: {customer_name}\n")
            file.write(f"Date: {datetime.now()}\n")
            file.write("-------------------------\n")
            for item in self.items:
                file.write(f"{item.menu_item.name} x{item.quantity} = ${item.get_total_price():.2f}\n")
            file.write("-------------------------\n")
            file.write(f"Total: ${total:.2f}\n")
            file.write("Thank you! Please visit again.\n")
        print(f"Bill saved as {filename} ✅")

    def get_bill_text(self, customer_name):
        from datetime import datetime
        total = sum(item.get_total_price() for item in self.items)
        lines = [
            "=== RESTAURANT BILL ===",
            f"Customer: {customer_name}",
            f"Date: {datetime.now()}",
            "-------------------------"
        ]
        for item in self.items:
            lines.append(f"{item.menu_item.name} x{item.quantity} = ${item.get_total_price():.2f}")
        lines.append("-------------------------")
        lines.append(f"Total: ${total:.2f}")
        lines.append("Thank you!")
        return "\n".join(lines)
