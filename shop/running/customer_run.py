from shop import RUNNING, clear_screen, HELP_COSTUMER, Customer, products

costomer_user = Customer()

def customer_run():
    """
    This function runs the customer process.

        Parameters:
            None

    Returns:
            None
    """
    clear_screen()
    print(f"welcome--------------")
    while RUNNING:
        user_command = input("what do you want to do:").lower()
        if user_command == "help":
            clear_screen()
            costomer_user.is_help()

        elif user_command == "exit":
            break

        elif user_command == "remove":
            clear_screen()
            try:
                name = input("Please enter your product name: ").title()
            except ValueError:
                print("The input is wrong, please be careful!")
            else:
                remove_result = costomer_user.remove_product(name)
                if remove_result:
                    print(f"{name} has been successfully removed from your list")

        elif user_command == "add":
            clear_screen()
            try:
                name, number_purchases = input("Please enter with a space Name//Number: ").title().split()
                number_purchases = int(number_purchases)
            except ValueError:
                print("The input is wrong, please be careful!")
            else:
                add_result = costomer_user.add_product(name, number_purchases)
                if add_result:
                    if products[name]["stock"] > number_purchases:
                        print(f"{name} has been successfully added to your list")
                    else:
                        print("The stock of the product is less than you want")

        elif user_command == "show":
            clear_screen()
            backet = costomer_user.basket
            for product in backet:
                print(product)
                print(f"    {backet[product]}")
        
        elif user_command == "factor":
            clear_screen()
            costomer_user.factor()
        
        elif user_command == "search":
            clear_screen()
            try:   
                name = input("Please enter your product name: ").title()
                search_result = costomer_user.search_product(name)
                print(search_result)
            except ValueError:
                    print("The input is wrong, please be careful!")

        elif user_command == "display":
            clear_screen()
            costomer_user.show_products(products)       

        else:
            print("The entered command is not correct!")

