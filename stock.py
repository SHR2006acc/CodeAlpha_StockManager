import os


def click():
    input("Click Enter Button")
    os.system("cls")


def option():
    print("- Type 1 to show the stock")
    print("- Type 2 to Update the stock")
    print("- Type 3 to Calculate the totale investement ")
    print("- Type 4 to leave the program")


def choice_option():
    choice = 0
    while choice <= 0 or choice > 5:
        option()
        try:
           choice = int(input("-> "))
        except:
            choice = 0
    return choice


def print_stock(stock):
    os.system("cls")
    print("Stock : ")
    for product, details in stock.items():
        print("--"*10)
        print(f" - Product : {product}")
        print(f" * Quantity : {details['quantity']}")
        print(f" * Price : {details['price']} $")
    print("--"*10)


def update_options():
    os.system("cls")
    print("Type 1 to add item")
    print("Type 2 to delete item ")
    print("Type 3 to update item's data ")


def update_choice():
    choice = 0
    while choice != 1 and choice != 2 and choice != 3:
        update_options()
        choice = int(input("Enter your choice : "))
    return choice


def isExist(stock, product):
    if product in stock:
        return True
    else:
        return False


def investment(stock):
    if len(stock) == 0:
        return 0
    else:
        s = 0
        for product, details in stock.items():
            s += details["price"] * details["quantity"]
        return s


stock = {
    # "item":{
    #    "price":12,
    #    "quantity":12
    # }
}
leave = False
while not leave:
    choice = choice_option()
    if choice == 4:
        leave = True
    elif choice == 1:
        if len(stock) == 0:
            print("The stock is empty")
            click()
        else:
            print_stock(stock)
            click()
    elif choice == 2:
        n = update_choice()
        if n == 1:
            os.system("cls")
            product = input("Type the new product : ")
            product = product.lower()
            if isExist(stock, product):
                print(f"Product {product} already exist on the stock ")
                click()
            else:
                quantity = int(input("Enter the quantity : "))
                price = int(input("Enter the price : "))
                stock[product] = {"quantity": quantity, "price": price}
                click()
        elif n == 2:
            os.system("cls")
            product = input("Type the product that you want to delete : ")
            product = product.lower()
            if not isExist(stock, product):
                print(f"Product {product} doesn't exist on the stock ")
                click()
            else:
                os.system("cls")
                del stock[product]
                print("Deletion operation run succefully")
                click()
        else:  # n==3
            os.system("cls")
            product = input("Type the product : ")
            product = product.lower()
            if not isExist(stock, product):
                print(f"Product {product} doesn't exist on the stock ")
                click()
            else:
                quantity = int(input("Enter the quantity : "))
                price = int(input("Enter the price : "))
                stock[product] = {"quantity": quantity, "price": price}
                click()
    else:
        os.system("cls")
        print(f"Total investment : {investment(stock)} $")
        click()
