from test import  Store, Shop, Request , Storage



a = [
   {"item":"яблоко",
   "value":10
   },
   {"item":"груша",
   "value":6
   },
   {"item":"апельсин",
   "value":9
   }
]

store = Store(a)
shop = Shop(a)
request = Request(input(),input(),input(),input())
print(request.__repr__())
shop.add("мясо", 1)
print(shop.get_unique_items_count())
print(shop.get_items())
print(shop.get_free_space())
