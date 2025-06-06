from datetime import datetime

def collect_review(customer_name):
    review = input("\n📝 We value your feedback! Leave a short review (or press Enter to skip): ").strip()
    if review:
        with open("reviews.txt", "a", encoding="utf-8") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {customer_name}: {review}\n")
        print("✅ Thank you for your review!")
    else:
        print("⏩ No review submitted.")

def show_reviews(num=5):
    print("\n📋 Recent Customer Reviews:")
    try:
        with open("reviews.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No reviews found.")
                return
            for line in lines[-num:]:
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print("No reviews found.")
