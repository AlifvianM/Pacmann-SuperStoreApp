from transaction import Transactions


if __name__ == "__main__":
    transaction = Transactions()

    print(f"Hello User {transaction.id}")
    print("Please add some items")

    item_list = []
    item = {}
    while True:
        item_name = input("Item Name :")
        count = int(input("Count :"))
        price = int(input("Price :"))

        item[item_name] = {
            "count":count,
            "price":price
        }

        item_list.append(item)
        print(f"Item ={item_name}")
        print(f"Count ={count}")
        print(f"Price ={price}")
        
        print(item_list)

        if input("add again ?(y/n)") != "y":
            transaction.add_items(items=item_list)
            break
        else:
            continue
    
    while True:
        next_step = int(input(
        """
            what you want to do next ?
            [1] edit item
            [2] delete item
            [3] reset chart  
            [4] finish
        """
        ))

        if next_step == 1:
            transaction.show_cart()
            name = input("what item you want to edit ?")
            if transaction.check_list_item(item_name=name):
                item_name = input("Item Name :")
                count = int(input("Count :"))
                price = int(input("Price :"))
            
                print(f"Item ={item_name}")
                print(f"Count ={count}")
                print(f"Price ={price}")

                transaction.edit_item(name=name, item=item_name, count=count, price=price)
        
        if next_step == 2:
            dele = input("What item you want to delete ?")
            transaction.delete_item(item=dele)

        if next_step == 3:
            print("Reset Chart")
            transaction.reset_cart()

        if next_step == 4:
            print("Finish Process")
            transaction.show_cart()
            break