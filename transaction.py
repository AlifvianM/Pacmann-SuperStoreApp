import uuid
# from typing import Union

class Transactions:
    
    def __init__(self) -> None:
        self.id = uuid.uuid1()
        self.items = {}

    def show_cart(self) -> None:
        """
        Show list of cart.
        """
        # print(self.items.keys())
        print(f"User ID :{self.id}")
        print("-"*30)
        print("|", "Item Name", "|", "Count", "|", "Price", "|", "Total", "|")
        print("-"*30)
        for key,val in self.items.items():
            print("|",key, "|", val["count"], "|", val["price"], "|", val["count"]*val["price"], "|")

        self.total_price()

    def add_items(self, items:list) -> None:
        """
        This function is made for adding item to cart list

        items: list
            list of items that will buy by user
        """
        try:
            for item in items:
                for key,val in item.items():
                        self.items[key] = val
        except:
            raise

        print(self.items)
        self.show_cart()

    def edit_item(self, name:str, item:str=None, count:int=None, price:int=None) -> None:
        """
        This function is made for editing item list in cart by keys.

        name: str
            the name of key in list
        item: str
            the name for replacing keys or item name
        count: int
            value that will replace 'count' key value
        price: int
            value that will replace 'price' key value
        """
        try:
            if item is not None and type(item) == str:
                self.items[item] = self.items.pop(name)
            else:
                raise Exception(f"key {item} is not str")

            if count is not None and type(count) == int:
                self.items[item]["count"] = count
            else:
                raise Exception(f"key {count} is not int")

            if price is not None and type(price) == int:
                self.items[item]["price"] = price
            else:
                raise Exception(f"key {price} is not int")

            
        except KeyError:
            raise Exception(f"key {name} not found")
            
        
        self.show_cart()

    def delete_item(self, item:str):
        """
        This function is made for deleteing item in list of cart by inputing name of item and pop it.

        item: str
            value that will delete key / item name.
        """
        
        list_cart = list(self.items.keys())
        try:
            self.items.pop(item)
        except:
            raise Exception('Item is not in list.')
        self.show_cart()
        
    def reset_cart(self) -> None:
        """
        This function is made for reseting list of cart that user just add. Clear all the item inside 'self.items'.
        """
        self.items = {}
        print("Item has been reset")
        self.show_cart()

    def total_price(self) -> None:
        """
        This function is made for calculate the price total of cart
        
        var
        ----
        total_price -> will show the total of price
        """


        total_price = []
        list_cart = list(self.items.keys())
        
        for item in list_cart:
            total_price.append(self.items[item]["count"]*self.items[item]["price"])

        if sum(total_price) > 500000:
            print(f"You get 10% dicsount !\nTotal : {sum(total_price) - (0.1 * sum(total_price))}")
        elif sum(total_price) > 300000:
            print(f"You get 8% dicsount !\ntotal : {sum(total_price) - (0.08 * sum(total_price))}")
        elif sum(total_price) > 200000:
            print(f"You get 8% dicsount !\ntotal : {sum(total_price) - (0.05 * sum(total_price))}")
        else:
            print(f"Total : {sum(total_price)}")

    def check_list_item(self, item_name):
        list_cart = list(self.items.keys())

        if item_name in list_cart:
            return True
        else:
            print(f"There are no {item_name} in cart")