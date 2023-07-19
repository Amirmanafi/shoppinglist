from shop import (
Validation,
products,
RUNNING,
Admin,
clear_screen
)


# Create instances of Validation and Admin classes
validate = Validation()
user = Admin()

def admin_run(username: str, password: str) -> None:
    """
    Run the admin interface.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """
    # Validate the user credentials
    if validate.validate_user(username, password):
        print(f"welcome {username}")
        print("---------------------------------------")
        while RUNNING:
            # Prompt for user command
            user_command = input("what do you want to do:").lower()
            if user_command == "help":
                clear_screen()
                user.is_help()

            elif user_command == "exit":
                break

            elif user_command == "show":
                user.show_products(products)

            elif user_command == "add":
                clear_screen()
                try: 
                    name, price, stock = input("Please enter with a space Name//Price/Stock: ").title().split()
                    price, stock = int(price), int(stock)
                except:
                        print("The input is wrong, please be careful!")
                else:
                    add_message = user.add_product(products, name, price, stock)
                    print(add_message)

            elif user_command == "search":
                clear_screen()
                name = input("please enter product name: ").title()
                search_result = user.search_product(products, name)
                print(search_result)

            elif user_command == "remove":
                name = input("please enter product name: ")
                remove_result = user.remove_product(name)
                print(remove_result)

            elif user_command == "edit":
                clear_screen()
                try: 
                    name, price, stock = input("Please enter with a space Name//Price/Stock: ").title().split()
                    price, stock = int(price), int(stock)
                    user.edit_product(name, price, stock)
                except:
                        print("The input is wrong, please be careful!")
                else:
                    print("The desired product was edited")

            else:
                print("The entered command is not correct!")
    else:
        print("This account does not exist!")