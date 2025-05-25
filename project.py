from restaurant import Menu, Order
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk

def create_bill_image(bill_text, filename="bill.png"):
    # Create an image large enough for the bill text (adjust size if needed)
    img = Image.new('RGB', (400, 300), color='white')
    d = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except:
        font = ImageFont.load_default()

    d.text((10, 10), bill_text, fill='black', font=font)
    img.save(filename)
    return filename

def show_image(filename):
    root = tk.Tk()
    root.title("Bill")

    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)

    panel = tk.Label(root, image=img)
    panel.image = img  # Keep reference!
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
                print("Invalid item ID. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    order.display_order()

    name = input("\nEnter your name to save the order: ")
    order.save_order_to_file(name)
    order.print_bill(name)

    bill_text = order.get_bill_text(name)
    filename = create_bill_image(bill_text)
    show_image(filename)

if __name__ == "__main__":
    main()
