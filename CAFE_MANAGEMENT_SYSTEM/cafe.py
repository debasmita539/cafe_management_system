class Menu:
    
    def __init__(self):
        self.food={
    'Margherita':100,
    'Beef Mushroom':180,
    'Chicken Lovers':150,
    'Extravaganza':180,
    'Cheese Mania':130,
    'American classic cheese burger':200,
    'American all star':200,
    'Meatzza':200,
    'Mexican Sizzler':200,
    'APPLE strudel':120  
}
    

        self.starter = {
    'Chocolate Lava':150,
    'Choco bread sticks':170,
    'Potato wedges':80,
    'Bread sticks':100,
    'Chick and cheese':120,
    'cheesy bread':85,
    'Chicken wings':95,
    'Noodles':120
        }
        self.drinks = {
            "Coffee": 100,
            "Tea": 80,
            "Juice": 90,
            "Soda": 50
        }

    def display_menu(self):
        print("------ Menu ------")
        print("Food:")
        for item, price in self.food.items():
            print(f"{item}: ₹{price}")
        print("\nStarter:")
        for item, price in self.starter.items():
            print(f"{item}: ₹{price}")
        print("\nDrinks:")
        for item, price in self.drinks.items():
            print(f"{item}: ₹{price}")
        print("------------------")


class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.registered = False  
    def mark_as_registered(self):
        self.registered = True

    def is_registered(self):
        return self.registered


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0

    def add_item(self, item, price):
        self.items.append((item, price))
        self.total += price

    def calculate_discount(self):
        if self.customer.is_registered():
            discount = self.total * 0.30
            self.total -= discount
            print(f"30% discount applied! Discount amount: ₹{discount}")

    def display_order(self):
        print("\n------ Your Order ------")
        for item, price in self.items:
            print(f"{item}: ₹{price}")
        print("------------------------")
        print(f"Total Amount to Pay: ₹{self.total}")


def take_order(category, menu, order):
    while True:
        if category == "food":
            item = input("Enter food item: ").strip().capitalize()
            if item in menu.food:
                order.add_item(item, menu.food[item])
            else:
                print("Item not found in the menu!")
        elif category == "starter":
            item = input("Enter starter item: ").strip().capitalize()
            if item in menu.starter:
                order.add_item(item, menu.starter[item])
            else:
                print("Item not found in the menu!")
        elif category == "drinks":
            item = input("Enter drink item: ").strip().capitalize()
            if item in menu.drinks:
                order.add_item(item, menu.drinks[item])
            else:
                print("Item not found in the menu!")

    
        another = input(f"Would you like to add another {category} item? (yes/no): ").strip().lower()
        if another != "yes":
            break


def main():
    menu = Menu()
    registered_customers = {
        "8334756271": Customer("Debasmita jena", "8334756271"),
        "8749274341": Customer("Gyanasmita jena", "8749274341")
    }

    print("Welcome to Pizzeria!!")
    print("Kindly fill the details")
    customer_name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")

    if phone_number in registered_customers:
        customer = registered_customers[phone_number]
        customer.mark_as_registered()
        print("Welcome back! You are a registered customer.")
    else:
        customer = Customer(customer_name, phone_number)
        print("New customer detected. No discount applicable.")

    # Display the menu
    menu.display_menu()
    order = Order(customer)
    while True:
        category = input("What would you like to order? (food/starter/drinks/exit): ").strip().lower()
        if category == "exit":
            break

        if category in ["food", "starter", "drinks"]:
            take_order(category, menu, order)
        else:
            print("Invalid category!")

    order.calculate_discount()
    order.display_order()
    print("Thank you for visiting!!")


if __name__ == "__main__":
    main()