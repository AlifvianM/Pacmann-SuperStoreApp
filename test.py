from main import Transactions

transactions = Transactions()
transactions.add_items([
    {
        "mobil":{
            "count":1,
            "price":120000
        }
    },
    {
        "sepeda":{
            "count":1,
            "price":120000
        }
    }
])
transactions.edit_item(name="mobil", item="motor", count=3, price=100000)
transactions.reset_cart()