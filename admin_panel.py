# admin_panel.py
from restaurant import Menu

menu = Menu()
menu.load_menu()

while True:
    print("\n--- Admin Panel ---")
    print("1. Show Menu")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update Item")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        menu.display_menu()
    elif choice == "2":
        name = input("Enter new item name: ")
        price = float(input("Enter price: "))
        menu.add_menu_item(name, price)
    elif choice == "3":
        item_id = int(input("Enter item ID to remove: "))
        menu.remove_menu_item(item_id)
    elif choice == "4":
        item_id = int(input("Enter item ID to update: "))
        new_name = input("Enter new name: ")
        new_price = float(input("Enter new price: "))
        menu.update_menu_item(item_id, new_name, new_price)
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
