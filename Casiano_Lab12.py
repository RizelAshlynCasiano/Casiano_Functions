def display_menu():
    menu = {
        "Kare-Kare": 150,
        "Sinigang": 120,
        "Lumpiang Shanghai": 100,
        "Pansit Canton": 130
    }
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: Php {price}")
    return menu

def calculate_total(price):
    print(f"Total cost: Php {price}")
    return price

def process_payment(total):
    while True:
        try:
            cash = float(input("Enter cash rendered: Php "))
            if cash >= total:
                change = cash - total
                print(f"Payment accepted. Change: Php {change:.2f}")
                break
            else:
                print(f"Insufficient payment. You need at least Php {total:.2f}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    menu = display_menu()

    while True:
        choice = input("Select an item from the menu: ").strip()
        if choice in menu:
            total = calculate_total(menu[choice])
            process_payment(total)
            break
        else:
            print("Invalid choice. Please select an item from the menu.")

if __name__ == "__main__":
    main()