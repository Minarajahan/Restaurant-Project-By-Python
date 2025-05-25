# project.py
from restaurant import Menu, Order

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
