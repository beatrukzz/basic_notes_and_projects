# concession stand program

menu = {
    "hot_dog": 3.50,
    "hamburger": 4.00,
    "soda": 1.50,
    "chips": 1.00,
    "candy": 1.25
}

cart = []
total_cost = 0.0


print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: £{value:.2f}") #:10 aligns the text to 10 characters wide
print("--------------------------")

while True:
    food = input("Enter an item to add to your cart (or 'done' to finish): ").strip().lower() 
    if food == "done":
        break
    elif menu.get(food)is not None:
        cart.append(food)

for food in cart:
    total_cost += menu.get(food, 0)
print(f"\nYour cart contains: {', '.join(cart)}")


print("\n---------- BILL ----------")
print(f"Total cost: £{total_cost:.2f}")





