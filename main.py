# main.py

from restaurant import Menu, Order
from review import collect_review, show_reviews
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk

def create_bill_image(bill_text, filename="bill.png"):
    lines = bill_text.split('\n')
    width = 400
    line_height = 20
    height = line_height * (len(lines) + 2)

    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except:
        font = ImageFont.load_default()

    y = 10
    for line in lines:
        draw.text((10, y), line, fill='black', font=font)
        y += line_height

    img.save(filename)
    return filename

def show_image(filename):
    root = tk.Tk()
    root.title("Bill")
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.image = img
    panel.pack()
    root.mainloop()

def main():
    menu = Menu()
    menu.load_menu()
    menu.display_menu()

    order = Order()
    while True:
        try:
            item_id = int(input("\nEnter item number to order (0 to finish): "))
            if item_id == 0:
                break
            item = menu.get_item_by_id(item_id)
            if item:
                quantity = int(input(f"Enter quantity for {item.name}: "))
                order.add_item(item, quantity)
            else:
                print("Invalid item ID.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if not order.items:
        print("No items ordered.")
        return

    order.display_order()
    customer_name = input("\nEnter your name to save the order: ")
    order.save_order_to_file(customer_name)
    order.print_bill(customer_name)

    bill_text = order.get_bill_text(customer_name)
    filename = create_bill_image(bill_text)
    show_image(filename)

    collect_review(customer_name)
    show_reviews()

if __name__ == "__main__":
    main()
