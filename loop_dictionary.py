products = {
    "apple": 0.99,
    "banana": 0.49,
    "orange": 0.79,
    "grapes": 2.99,
    "watermelon": 4.99
}

total_bill = 0.0

while True:
    item = input("Enter the item you want to purchase (or 'done' to finish): ")

    if item == "done":
        break

    price = products.get(item)
    print(price)

    if price:
        total_bill += price
        print(f"Added {item} to the cart. Price: {price}")
    else:
        print("Invalid item. Please try again.")

print(f"Total bill amount: ${total_bill:.2f}")
