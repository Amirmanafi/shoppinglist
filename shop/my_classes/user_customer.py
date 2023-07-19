from .product import Product
from shop import products, HELP_COSTUMER

class Customer(Product):
    basket = {}

    def __init__(self) -> None:
        pass

    def is_help(self) -> None:
        """
        Display help messages for the customer.
        """
        for help in HELP_COSTUMER:
            print(help)

    def add_product(self, product_name: str, number_purchases: int = 1) -> None:
        """
        Add a product to the customer's basket.

        Args:
            product_name (str): The name of the product.
            number_purchases (int, optional): The number of purchases. Defaults to 1.
        """
        self.product_name = product_name
        self.number_purchases = number_purchases
        if super().is_available(self.basket, product_name):
            if not super().is_available(products, product_name):
                self.basket[self.product_name] = {"number": self.number_purchases}
                return True
            else:
                print(f"{self.product_name} is not included in the list of store products")
        else:
            print(f"'{self.product_name}' from it existed before")

    def remove_product(self, product_name: str) -> bool:
        """
        Remove a product from the customer's basket.

        Args:
            product_name (str): The name of the product.

        Returns:
            bool: True if the product was successfully removed, False otherwise.
        """
        self.product_name = product_name
        if not super().is_available(self.basket, product_name):
            del self.basket[self.product_name]
            return True
        else:
            print(f"{self.product_name} is not in the list")
            return False

    def search_product(self, product_name: str) -> str:
        """
        Search for a product in the customer's basket.

        Args:
            product_name (str): The name of the product.

        Returns:
            str: A message indicating whether the product is in the list or not.
        """
        if super().is_available(self.basket, product_name):
            return f"'{self.product_name}' is not in the list"
        else:
            return f"'{self.product_name}' is in the list"
    
    def factor(self) -> None:
        """
        Calculate the total cost of the products in the customer's basket and print.
        """
        factor = 0
        for product, number in self.basket.items():
            number = number["number"]
            price = self.products[product]["price"]
            factor += price * number
        print(f"total:{factor}")

    def show_products(self, products:dict[dict]):
        """
        Display the products and their details.

        Args:
            products (dict): The dictionary containing the products.
        """
        self.products = products
        for item in products:
            print(item)
            print(f"      {self.products[item]}")
            print("-"* 40 )
