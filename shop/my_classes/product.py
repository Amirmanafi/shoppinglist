from shop import Validation
from shop import products


class Product(Validation):

    """
    Class representing a product in a shop.
    """

    def __init__(self) -> None:
        self.products = products
        self.result = True

    def add_product(self, product_list: dict[dict], name: str, price: int, stock: int= 0) -> str:
        """
                Add a new product to the product list.

                Args:
                    product_list (dict): The dictionary representing the product list.
                    name (str): The name of the product.
                    price (int): The price of the product.
                    stock (, optional): The stock quantity of the product. Defaults to 0.

                Returns:
                    str: A message indicating whether the product was successfully added or not.
                """

        self.product_list = product_list
        self.name = name
        self.price = price
        self.stock = stock
        validate = super().is_available(products, name)
        if validate:
            self.product_list[self.name] = {"price": self.price, "stock": self.stock}
            return f"'{self.name}' was added to the product basket"
        else:
            return "This product already existed!"

    def remove(self, product_name: str) -> str:
        """
        Remove a product from the product list.

        Args:
            product_name (str): The name of the product to be removed.

        Returns:
            str: A message indicating whether the product was successfully removed not.
        """

        self.product_name = product_name
        if not super().is_available(products, product_name):
            del products[self.product_name]
            remove_result = f"'{self.product_name}' has been removed from your product list"
        else:
            remove_result = f"'{self.product_name}' does not exist!"
        return remove_result

    def edite(self, name:str, price: int = 0, stock: int = 0) -> None:
        """
        Edit the details of a product.

        Args:
            name (str): The name the product to be edited.
            price (int, optional): The new price of the product. Defaults to 0.
            stock (int, optional): The new stock quantity of the product. Defaults to 0.
        """
        remove_result = self.remove(name)
        if "removed" in remove_result:
            self.add_product(products, name, price, stock)
