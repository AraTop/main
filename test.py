from abc import ABC , abstractmethod

storag = {
   "яблоко":9,
   "груша":8,
   "апельсин":2,
   "собачки":3
}    
b = {
   "мясо":1
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
   def __init__(self,items, capacity=1000):
      super().__init__(items, capacity)

   def add(self,name, value):
      numbers = 0
      for y, x in self._items.items():
         numbers += x
      if numbers >= 1000:
         return "Склад переполнен"
      
      if numbers + value >= 1000:
         return "Не хватает на складе, попробуйте заказать меньше"

      if value < 1:
         return "Некоректное значение"
      
      self._items[name] = value

   def remove(self, key, value):
      if value < 1:
         return "количество не может быть меньше нуля"
      
      if self._items.get(key):
         number = self._items.get(key)
         self._items[key] = number - value
         return 'Курьер забрал'
         
   def get_free_space(self):
      number = []
      for key, value in self._items.items():
         number.append(value)

      sum_ = self._capacity - sum(number)
      if sum_ > 0:
         return sum_
      elif sum_ < 0:
         return f"Склад переполнен" 
      
   def get_items(self):
      print("в Складе хранится:\n")
      for key, value in self._items.items():
         print(key, value)
      return ""
   
   def get_unique_items_count(self):
      number = []
      for key, value in self._items.items():
        number.append(key)
      return len(set(number))
   
   def give_self(self, key):
      return self._items.get(key)

class Shop(Store):
   def __init__(self, items, capacity=20):
      super().__init__(items, capacity)

   def add(self,name, value):
      numbers = 0
      for y, x in self._items.items():
         numbers += x
      if numbers >= 20:
            return "Магазин переполнен"
      
      if numbers + value >= 20:
         return "В магазине недостаточно места, попобуйте что то другое"
      
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
         return "В магазине недостаточно места, попобуйте что то другое"
         
   
   def get_items(self):
      print("в магазине хранится:\n")
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

        self.store = Store(storag)
        self.shop = Shop(b)

   def get_data(self, user_str):
      return user_str.split(" ")

   def add(self):
      if self.shop.get_free_space() == "В магазине недостаточно места, попобуйте что то другое":
         return "В магазин недостаточно места, попобуйте что то другое"
      
      if self.amount <= 0:
         return 'Неверное кол-во'
      
      if self.store.give_self(self.product) - self.amount >= 0:
         print("Нужное количество есть на складе")
         print(f"Курьер забрал {self.amount} {self.product} со склад")
         print(f"Курьер везет {self.amount} {self.product} со склад в магазин")
         print(f"Курьер доставил {self.amount} {self.product} в магазин")

         self.store.remove(self.product, self.amount)
         self.shop.add(self.product, self.amount)
      else:
         return "Не хватает на складе, попробуйте заказать меньше"
      
      return self.shop.get_items() , self.store.get_items()

      #print(self.store.get_items())
      #self.store.remove(self.product, self.amount)
      #print(self.store.get_items())
      
   def __repr__(self):
      return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'
