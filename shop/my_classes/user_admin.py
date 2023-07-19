from .product import Product
from shop import HELP_ADMIN


class Admin(Product):
    """
    Admin class inherits from the Product class and provides additional functionality for managing products.
    """
    def __init__(self) -> None:
        pass
    
    def is_help(self) -> None:
        """
        Prints the help messages for admin.
        """
        for help in HELP_ADMIN:
            print(help)
    
    def add_product(self, product_list: dict[dict], name: str, price: int = 0, stock: int = 0):
        """
        Adds a new product to the product list.

        Args:
            product_list (dict): The dictionary containing the product information.
            name (str): The name of the product.
            price (int, optional): The price of the product. Defaults to 0.
            stock (int, optional): The stock quantity of the product. Defaults to 0.

        Returns:
            dict: The updated product list.
        """
        return super().add_product(product_list, name, price, stock)

    def remove_product(self, product_name: str):
        """
        Removes a product from the product list.

        Args:
            product_name (str): The name of the product to be removed.

        Returns:
            bool: True if the product was successfully removed, False otherwise.
        """
        self.product_name = product_name
        return super().remove(product_name)

    def search_product(self, products, name):
        """
        Searches for a product in the product list.

        Args:
            products (dict): The dictionary containing the product information.
            name (str): The name of the product search for.

        Returns:
            str: The search result message indicating whether the product was found or not.
        """
        search_result = super().is_available(products, name)
        if search_result:
            search_result = f"The desired '{name}' was not found in the product list!"
        else:
            search_result = f"The desired '{name}' is in the product list"
        return search_result

    def edit_product(self, name: str, price:int, stock: int):
        """
        Edits the details of a product.

        Args:
            name (): The name of the product to edited.
            price (int): The new price of the product.
            stock (int): The new stock quantity of the product.
        """

        super().edite(name, price, stock)

    def show_products(self, products:dict[dict]):
        """
        Displays all the products in the product list.

        Args:
            products (dict): The dictionary containing the product information.
        """
        self.products = products
        for item in products:
            print(item)
            print(f"      {self.products[item]}")
            print("-"* 40 )
        