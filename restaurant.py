from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

class MenuItem:
    def __init__(self, item_id, name, price):
        self.id = item_id
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = []

    def load_menu(self):
        try:
            with open("menu.txt", "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        item_id = int(parts[0])
                        name = parts[1]
                        price = float(parts[2])
                        self.items.append(MenuItem(item_id, name, price))
        except FileNotFoundError:
            print("menu.txt file not found. Please create it with the menu items.")
            exit(1)

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
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def display_order(self):
        print("\nYour Order:")
        total = 0
        for item, qty in self.items.items():
            cost = item.price * qty
            total += cost
            print(f"{item.name} x{qty} = RMB {cost:.2f}")
        print(f"Total: RMB = {total:.2f}")

    def save_order_to_file(self, customer_name):
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bill_{customer_name}_{now}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Your Order:\n")
            total = 0
            for item, qty in self.items.items():
                cost = item.price * qty
                total += cost
                file.write(f"{item.name} x{qty} RMB = {cost:.2f}\n")
            file.write("-" * 40 + "\n")
            file.write(f"Total RMB = {total:.2f}\n")
        print(f"Bill saved as {filename} ✅")
        return filename

    def get_bill_text(self, customer_name):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lines = [f"Bill for {customer_name} ({now}):", ""]
        total = 0
        for item, qty in self.items.items():
            cost = item.price * qty
            total += cost
            lines.append(f"{item.name} x{qty} RMB = {cost:.2f}")
        lines.append("-" * 40)
        lines.append(f"Total RMB = {total:.2f}")
        return "\n".join(lines)

    def print_bill(self, customer_name):
        print("\n" + self.get_bill_text(customer_name))

    def save_bill_as_image(self, customer_name):
        bill_text = self.get_bill_text(customer_name)
        lines = bill_text.split('\n')

        width = 500
        padding = 20
        font_size = 18
        line_spacing = 10

        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        fallback_font = "arial.ttf"

        try:
            font = ImageFont.truetype(font_path, font_size)
        except:
            try:
                font = ImageFont.truetype(fallback_font, font_size)
            except:
                font = ImageFont.load_default()

        try:
            line_height = font.getbbox("A")[3] + line_spacing
        except AttributeError:
            line_height = font.getsize("A")[1] + line_spacing

        header_lines = ["Minara Cafe & Restaurant", "-" * 40]
        footer_lines = ["", "Thank you for dining with us!"]
        all_lines = header_lines + lines + footer_lines

        height = padding * 2 + line_height * len(all_lines)
        img = Image.new("RGB", (width, height), "#f9f9f9")
        draw = ImageDraw.Draw(img)

        draw.rectangle([0, 0, width - 1, height - 1], outline="#cccccc")

        y = padding
        for line in all_lines:
            draw.text((padding, y), line, font=font, fill="black")
            y += line_height

        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bill_image_{customer_name}_{now}.png"
        img.save(filename)
        print(f"🖼️ Bill Slip {filename}")
        return filename
