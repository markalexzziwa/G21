print("Welcome to our E-Commerce Store!")
username = input("Please enter your name: ")
password = input("Please enter your password: ")
products =["TV", "laptop", "Subwoofer", "Fibre Cables", "Smartphone", "Headphones", "Speakers", "Router", "Printer", "Sony Camera"]
locations = ["kampala", "masaka", "mukono", "gulu", "busia"]
locationdiscounts = {
    "kampala": 0.10,
    "masaka": 0.15,
    "mukono": 0.20,
    "gulu": 0.25,
    "busia": 0.30
}
if username == "admin" and password == "adminpwd123":
    print("Login successful! Welcome, admin.")
elif username == "cashier" and password == "cashpwd123":
    print("Login successful! Welcome, cashier.")
    total_amount = float(input("Please enter the total amount of your purchase: "))
    print("Login successful! Welcome, customer.")
else:
    print("Login failed! Invalid username or password.")

if username in ["admin", "customer"]:
    print("Here are the available products:")
    for product in products:
        print("-> " + product)
    print("supported locations: ", ", ".join(locations))

if username in ["admin", "cashier"]:
    total_amount = float(input("Please enter the total amount of your purchase: "))
    shipping_cost = int(input("Please enter the shipping cost: "))
    coupon_code = input("Please enter your coupon code: ")
    if coupon_code == "d20t10":
        print("Coupon code Valid and applied successfully!")    
    elif coupon_code == "F00t20":
        print("Coupon code Valid and applied successfully!")
    else:
        print("Invalid coupon code. No discounts applied.")
    match coupon_code:
        case "d20t10":
            print("You have received a 20% discount on your purchase!")
            discount_amount = total_amount * 0.20
            total_amount -= discount_amount
            tax = total_amount * 0.10
            total_amount += tax
            print(f"Total amount after discount and tax is: UGX.{total_amount:.2f}")
            total_cost = total_amount + shipping_cost
            location = input("Please enter your location: ").lower()
            if location in locationdiscounts:
                location_discount = locationdiscounts[location]
                print(f"You have received an additional {location_discount*100:.0f}% discount based on your location!")
                total_amount -= total_amount * location_discount
            print(f"Your total cost including shipping is: UGX.{total_cost:.2f}")
        case "F00t20":
            print("You have received free shipping on your order!")
            tax = total_amount * 0.20
            total_amount += tax
            total_cost = total_amount
            print(f"Your total cost including shipping is: UGX.{total_cost:.2f}")
        case _:
            print("Invalid coupon code. No discounts applied.")
        