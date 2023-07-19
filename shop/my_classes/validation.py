from shop import products


class Validation():
    """
    Class for user validation and product availability checks.
    """
    admin_list = [("amir", "1234"), ("ali", "0258"), ("mohammad", "456321"), ("sajad", "741258")]
    result = True
    
    def __init__(self) -> None:
        pass

    def validate_user(self, username, password) -> bool:
        """
        Validate the user credentials.

        Args:
            username (str): The username.
            password (str): The password.

        Returns:
            bool: True if the user is valid, False otherwise.
        """

        self.__password = password
        self.username = username
        for admin in self.admin_list:
            if self.username == admin[0] and self.__password == admin[1]:
                break
        else:
            self.result = False
        return self.result

    def is_available(self, products: dict[dict], product_name:str) -> bool:
        """
        Check if a product is available in the product list.

        Args:
            products (dict): The dictionary containing the products.
            product_name (str): The name of the product.

        Returns:
            bool: True if the product available, False otherwise.
        """
        self.product_name = product_name
        self.products = products
        if self.product_name in self.products:
            return False
        return True

    def in_stock(self, products: dict[dict], product_name: str):
        """
        Check if a product is in stock.

        Args:
            products (dict): The dictionary containing the products.
            product_name (str): The name of the product.

        Returns:
            bool: True if the product is stock, False otherwise.
        """
        self.result = True 
        self.product_name = product_name
        self.products = products
        if not self.products[self.product_name] > 0:
             self.result = False
        return self.result
