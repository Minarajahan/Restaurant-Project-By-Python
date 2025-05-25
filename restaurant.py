# restaurant.py

class MenuItem:
    def __init__(self, item_id, name, price):
        self.id = item_id
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = []

    def load_menu(self, filename="menu.csv"):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    item_id, name, price = parts
                    self.items.append(MenuItem(int(item_id), name, float(price)))

    def display_menu(self):
        print("\nMenu:")
        for item in self.items:
            print(f"{item.id}. {item.name} - RMB {item.price:.2f}")

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def display_order(self):
        print("\nYour Order:")
        total = 0
        for item, qty in self.items:
            subtotal = item.price * qty
            print(f"{item.name} x{qty} = RMB {subtotal:.2f}")
            total += subtotal
        print(f"Total: RMB{total:.2f}")

    def save_order_to_file(self, customer_name):
        from datetime import datetime
        filename = "orders.txt"
        total = sum(item.price * qty for item, qty in self.items)
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - {customer_name}: RMB{total:.2f}\n")

    def get_bill_text(self, customer_name):
        from datetime import datetime
        lines = [f"Customer: {customer_name}", f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ""]
        total = 0
        for item, qty in self.items:
            subtotal = item.price * qty
            lines.append(f"{item.name} x{qty} = RMB {subtotal:.2f}")
            total += subtotal
        lines.append(f"\nTotal: RMB{total:.2f}")
        return '\n'.join(lines)

    def print_bill(self, customer_name):
        from datetime import datetime
        filename = f"bill_{customer_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        bill_text = self.get_bill_text(customer_name)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(bill_text)
        print(f"Bill saved as {filename} ✅")
