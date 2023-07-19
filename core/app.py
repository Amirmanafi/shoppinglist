from shop import RUNNING, admin_run, customer_run
from getpass import getpass
from time import sleep

def main() -> None :
    """
    The main function of the program.
    It prompts the user to choose between being an admin a customer,
    and then calls the appropriate functions based on the user's choice.
    """
    while RUNNING:
            user = input("Are you an admin or a customer: ").lower()
            if user == "admin":
                username = input("please enter your username: ").lower()
                password = getpass("pelase enter your password: ").lower()
                admin_run(username, password)
            elif user == "customer":
                customer_run()
            else:
                print("The entered command is not correct!")
                sleep(1)
