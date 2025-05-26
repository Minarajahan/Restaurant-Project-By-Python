from restaurant import Menu, Order
from review import collect_review, show_reviews

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
                if quantity > 0:
                    order.add_item(item, quantity)
                else:
                    print("Quantity must be positive.")
            else:
                print("Invalid item number. Try again.")
        except ValueError:
            print("Please enter valid numbers.")

    if not order.items:
        print("No items ordered. Goodbye!")
        return

    order.display_order()

    name = input("\nEnter your name to save the order: ").strip()
    if not name:
        name = "Customer"

    order.save_order_to_file(name)
    order.print_bill(name)
    order.save_bill_as_image(name)  # <-- save bill as image here

    collect_review(name)
    show_reviews()

if __name__ == "__main__":
    main()
