from main import Transactions

transactions = Transactions()

print('-'*5,'ADD ITEM','-'*5)
transactions.add_items([
    {
        "Ayam Goreng":{
            "count":2,
            "price":20000
        }
    },
    {
        "Pasta Gigi":{
            "count":3,
            "price":15000
        }
    }
])

print("\n")
print('-'*5,'DELETE ITEM','-'*5)
transactions.delete_item(item="Pasta Gigi")

print("\n")
print('-'*5,'TOTAL PRICE','-'*5)
transactions.show_cart()

print("\n")
print('-'*5,'EDIT ITEM','-'*5)
transactions.edit_item(name="Ayam Goreng", item="Sepeda Motor 1000cc", count=3, price=100000)

print("\n")
print('-'*5,'RESET CHART','-'*5)
transactions.reset_cart()


