from abc import ABC , abstractmethod

a = {
   "яблоко":10,
   "груша":6,
   "апельсин":1000
}   

b = {
   "мясо": 2,
   "Молоко":3
}   


v = {
   "кукла": 6,
   "машинка":1
}   


class Storage(ABC):
   def __init__(self, items,capacity=1000):
      self._items = items
      self._capacity = capacity
   
   @abstractmethod
   def add(self,name, value):
      numbers = 0
      for y, x in self._items.items():
         numbers += x
      if numbers >= self._capacity:
         return "склад переполнен"
      
      if value < 1:
         return "некоректное значение"
      
      self._items[name] = value
   
   @abstractmethod
   def remove(self, key, value):
      if value < 1:
         return "количество не может быть меньше нуля"
      else:
            try:
               number = self._items.get(key)
               self._items[key] = number - value
               return self.get_items()
            except Exception as s:
               return "Не хватает на складе, попробуйте заказать меньше"

   @abstractmethod
   def get_free_space(self):
      number = []
      for key, value in self._items.items():
         number.append(value)

      sum_ = self._capacity - sum(number)
      if sum_ > 0:
         return f"Всего мест: {sum_}"
      elif sum_ <= 0:
         return f"склад забит" 
   
   @abstractmethod
   def get_items(self):
      print("в склад хранится:\n")
      for key, value in self._items.items():
         print(key, value)
      return ""
      
   @abstractmethod
   def get_unique_items_count(self):
      number = []
      for key, value in self._items.items():
        number.append(key)
      return len(set(number))

class Store(Storage):
   def __init__(self,items, capacity=100):
      super().__init__(items, capacity)

   def add(self,name, value):
      numbers = 0
      for y, x in self._items.items():
         numbers += x
      if numbers >= 100:
         return "В Store недостаточно места, попобуйте что то другое"
      
      if numbers + value >= 20:
         return "В Shop недостаточно места, попобуйте что то другое"

      if value < 1:
         return "некоректное значение"
      
      if self.get_unique_items_count() >= 5:
         return "уже есть 5 разных товаров"
      
      self._items[name] = value

   def remove(self, key, value):
      if value < 1:
         return "количество не может быть меньше нуля"
      else:
            try:
               number = self._items.get(key)
               self._items[key] = number - value
               return self.get_items()
            except Exception as s:
               return str(s)

   def get_free_space(self):
      number = []
      for key, value in self._items.items():
         number.append(value)

      sum_ = self._capacity - sum(number)
      if sum_ > 0:
         return f"Всего мест: {sum_}"
      elif sum_ < 0:
         return f"В Store недостаточно места, попобуйте что то другое" 
      
   def get_items(self):
      print("в Store хранится:\n")
      for key, value in self._items.items():
         print(key, value)
      return ""
   
   def get_unique_items_count(self):
      number = []
      for key, value in self._items.items():
        number.append(key)
      return len(set(number))

class Shop(Storage):
   def __init__(self, items, capacity=20):
      super().__init__(items, capacity)

   def add(self,name, value):
      numbers = 0
      for y, x in self._items.items():
         numbers += x
      if numbers >= 20:
            return "В Shop недостаточно места, попобуйте что то другое"
      
      if numbers + value >= 20:
         return "В Shop недостаточно места, попобуйте что то другое"
      
      if value < 1:
         return "некоректное значение"
      
      if self.get_unique_items_count() >= 5:
         return "уже есть 5 разных товаров"
      
      self._items[name] = value
   
   def remove(self, key, value):
      if value < 1:
         return "количество не может быть меньше нуля"
      else:
            try:
               number = self._items.get(key)
               self._items[key] = number - value
               return self.get_items()
            except Exception as s:
               return str(s)
            
   def get_free_space(self):
      number = []
      for key, value in self._items.items():
         number.append(value)

      sum_ = self._capacity - sum(number)
      if sum_ > 0:
         return f"Всего мест: {sum_}"
      elif sum_ <= 0:
         return f"В Shop недостаточно места, попобуйте что то другое" 
   
   def get_items(self):
      print("в Shop хранится:\n")
      for key, value in self._items.items():
         print(key, value)
      return ""
   
   def get_unique_items_count(self):
      number = []
      for key, value in self._items.items():
        number.append(key)
      return len(set(number))
   
class Request:
   def __init__(self, user_str):
        data = self.get_data(user_str)
        self.from_ = data[4]
        self.to = data[6]
        self.amount = int(data[1])
        self.product = data[2]

        self.store = Store(b)
        self.shop = Shop(v)

   def get_data(self, user_str):
      return user_str.split(" ")

   def add(self):
      
      if self.shop.get_free_space() == "В Shop недостаточно места, попобуйте что то другое":
         return "В магазин недостаточно места, попобуйте что то другое"
      if self.store.get_free_space() == "В Store недостаточно места, попобуйте что то другое":
         return "В магазин недостаточно места, попобуйте что то другое"

      self.shop.add(self.product,self.amount)
      self.store.add(self.product,self.amount)

      return self.shop.get_items() , self.store.get_items()

   def __repr__(self):
      return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'
