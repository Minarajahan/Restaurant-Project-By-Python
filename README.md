# 🍽️ Restaurant Management System

A simple yet feature-rich **Restaurant Management System** built with **Python**, designed to streamline order management, billing, and customer feedback in a restaurant environment. This console-based system supports menu loading from a file, order processing with quantity tracking, bill generation in both text and image format, and review collection with storage.

---

## 🔧 Features

- 📋 Load menu items from `menu.txt`
- 🧾 Order placement with item ID and quantity
- 💵 Automatic bill calculation and display
- 🗂️ Save bills as both text and image (PNG)
- 🌟 Customer feedback and review collection
- 🧠 Basic review display from `reviews.txt`

---

## 📁 Project Structure

restaurant_management/
│
├── main.py # Entry point
├── restaurant.py # Core logic: Menu & Order classes
├── review.py # Feedback collection & display
├── menu.txt # List of food & drink items
├── reviews.txt # Stores customer reviews
├── bill_.txt # Auto-generated order bills (text)
├── bill_image_.png # Auto-generated order bills (image)
└── README.md # Project documentation


🧑‍💻 Example Usage
Sample Menu (menu.txt)
Copy
Edit
1,Burger,5.99
2,Pizza,8.99
3,Pasta,6.49
4,Coffee,2.50
5,Lemon Juice,3.00
6,Tea,2.00


Terminal Interaction

Menu:
1. Burger - RMB 5.99
2. Pizza - RMB 8.99
...

Enter item number to order (0 to finish): 2
Enter quantity for Pizza: 2

Enter your name to save the order: Alice

Your Order:
Pizza x2 = RMB 17.98
Total: RMB = 17.98

Bill saved as bill_Alice_20250526_142301.txt ✅
🖼️ Bill Slip bill_image_Alice_20250526_142301.png
🖼️ Sample Bill Image
The system generates a PNG bill with restaurant branding using Pillow:


from PIL import Image, ImageDraw, ImageFont

# Sample function from restaurant.py
def save_bill_as_image(customer_name):
    ...
    img.save(f"bill_image_{customer_name}_{timestamp}.png")
🗣️ Customer Review Feature
After placing an order, the system asks for customer feedback.

The review is saved in reviews.txt and recent reviews are shown to the next customer.





# review.py
def collect_review(customer_name):
    review = input("Leave a review: ")
    with open("reviews.txt", "a") as file:
        file.write(f"{datetime.now()} | {customer_name}: {review}\n")
📌 Requirements
Python 3.6+

Pillow library (for image bill generation)

Install with:

pip install pillow
👩‍💻 Developed by
Minara Jahan
Student of Software Engineering
Project for Final Evaluation (Python)


📃 License
This project is for educational purposes only.






