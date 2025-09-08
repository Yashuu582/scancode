# Grocery Store Management (Intermediate Version - Simple Print)

# Store items with price and quantity
store = {
    "Milk": {"price": 40, "quantity": 10},
    "Bread": {"price": 25, "quantity": 15},
    "Eggs": {"price": 5, "quantity": 50},
    "Rice": {"price": 60, "quantity": 20},
    "Sugar": {"price": 45, "quantity": 30}
}

def add_item():
    name = input("Enter item name: ").strip()
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    store[name] = {"price": price, "quantity": quantity}
    print(f"{name} added successfully!\n")

def view_items():
    if not store:
        print("No items in store!\n")
    else:
        print("\n--- Items in Store ---")
        for name, details in store.items():
            print(name, "- Price: Rs.", details["price"], ", Quantity:", details["quantity"])
        print()

def buy_item():
    if not store:
        print("No items available to buy!\n")
        return
    
    total = 0
    print("\n--- Start Shopping ---")
    while True:
        name_input = input("Enter item name to buy (or 'done' to finish): ").strip()
        if name_input.lower() == "done":
            break

        # Find item in store ignoring case
        found_item = None
        for item in store:
            if item.lower() == name_input.lower():
                found_item = item
                break

        if found_item:
            qty = int(input("Enter quantity: "))
            if qty <= store[found_item]["quantity"]:
                cost = store[found_item]["price"] * qty
                total += cost
                store[found_item]["quantity"] -= qty
                print(f"Added {qty} x {found_item} = Rs.{cost}")
            else:
                print(f"Sorry! Only {store[found_item]['quantity']} {found_item} left in stock.")
        else:
            print("Item not found!")
    
    print("\n--- Final Bill ---")
    print(f"Total Amount: Rs.{total}\n")

def main():
    while True:
        print("\n--- Supermarket Menu ---")
        print("1. Add Item")
        print("2. View Items")
        print("3. Buy Items")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            buy_item()
        elif choice == "4":
            print("Thank you for visiting our Supermarket!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
