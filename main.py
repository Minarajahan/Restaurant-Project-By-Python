from restaurant import Menu, Order
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
from review import collect_review  # ✅ NEW: Import review

def create_bill_image(bill_text, filename="bill.png"):
    lines = bill_text.split('\n')
    width = 400
    line_height = 20
    height = line_height * (len(lines) + 2)

    img = Image.new('RGB', (width, height), color='white')
    d = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except:
        font = ImageFont.load_default()

    y_text = 10
    for line in lines:
        d.text((10, y_text), line, fill='black', font=font)
        y_text += line_height

    img.save(filename)
    return filename

def show_image(filename):
    root = tk.Tk()
    root.title("Bill")

    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)

    panel = tk.Label(root, image=img)
    panel.image = img  # keep a reference
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

    if not order.items:
        print("No items ordered. Exiting.")
        return

    order.display_order()

    name = input("\nEnter your name to save the order: ")
    order.save_order_to_file(name)
    order.print_bill(name)

    bill_text = order.get_bill_text(name)
    filename = create_bill_image(bill_text)
    show_image(filename)

    collect_review(name)  # ✅ Ask for review after bill is shown

if __name__ == "__main__":
    main()



#--------REVIEW-------
def create_review_image(name, rating, comment, filename="review.png"):
    from PIL import Image, ImageDraw, ImageFont

    width, height = 400, 200
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()

    y = 10
    draw.text((10, y), "CUSTOMER REVIEW", font=font, fill="black")
    y += 30
    draw.text((10, y), f"Name: {name}", font=font, fill="black")
    y += 25
    draw.text((10, y), f"Rating: {'★' * int(rating)}", font=font, fill="black")
    y += 25
    draw.text((10, y), f"Comment: {comment}", font=font, fill="black")
    y += 30
    draw.text((10, y), "Thank you for your feedback!", font=font, fill="green")

    img.save(filename)
    return filename
