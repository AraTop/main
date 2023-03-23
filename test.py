from abc import ABC , abstractmethod


class Storage(ABC):
   def __init__(self, items,capacity):
      self._items = items
      self._capacity = capacity
   
   @abstractmethod
   def add(self, name, value):
      numbers = 0
      for y in self._items:
         numbers += y["value"]
      if numbers >= 20:
            return "В магазине недостаточно места, попобуйте что то другое"
      
      if self.get_unique_items_count() >= 5:
         return "нет мест больше 5 предметов"
      
      self._items["value"] = value , self._items["value"] = value
      
      return self._items

   def remove(self, key, value=20):
      for items in self._items:
         if items["value"] < 0:
            break
         else:
            self._items.remove(key)

   @abstractmethod
   def get_free_space(self):
      value = []
      for y in self._items:
         value.append(y["value"])

      sum_ = self._capacity - sum(value)
      if sum_ > 0:
         return f"кол-во мест: {sum_}"
      elif sum_ < 0:
         return f"Не хватает на складе, попробуйте заказать меньше" 
   
   @abstractmethod
   def get_items(self):
      print("на складе хранится: ")
      for y in self._items:
         print(y["value"], y["item"])
      return ""
      
   @abstractmethod
   def get_unique_items_count(self):
      number = []
      for y in self._items:
        number.append(y["item"])
      return len(set(number))
   

class Store(Storage):
   def __init__(self,items, capacity=100):
      super().__init__(items, capacity)

   def add(self,name, value=100):
      numbers = 0
      for y in self._items:
         numbers += y["value"]
      if numbers >= 20:
            return "В магазине недостаточно места, попобуйте что то другое"
      
      if self.get_unique_items_count() >= 5:
         return "нет мест больше 5 предметов"
      
      self._items["value"] = value , self._items["value"] = value
      
      return self._items

   def remove(self, key, value=20):
      for items in self._items:
         if items["value"] < 0:
            break
         else:
            self._items.remove(key)

   def get_free_space(self):
      value = []
      for y in self._items:
         value.append(y["value"])

      sum_ = self._capacity - sum(value)
      if sum_ > 0:
         return f"кол-во мест: {sum_}"
      elif sum_ < 0:
         return f"В магазин недостаточно места, попобуйте что то другое" 
      
   def get_items(self):
      print("в магазине хранится: ")
      for y in self._items:
         print(y["value"], y["item"])
      return ""
   
   def get_unique_items_count(self):
      number = []
      for y in self._items:
        number.append(y["item"])
      return len(set(number))

class Shop(Storage):
   def __init__(self, items, capacity=20):
      super().__init__(items, capacity)

   def add(self,name, value=20):
      numbers = 0
      for y in self._items:
         numbers += y["value"]
      if numbers >= 20:
            return "В магазине недостаточно места, попобуйте что то другое"
      
      if self.get_unique_items_count() >= 5:
         return "нет мест больше 5 предметов"
      
      self._items["value"] = value , self._items["value"] = value

      return self._items
   
   def remove(self, key, value=20):
      for items in self._items:
         if items["value"] < 0:
            break
         else:
            self._items.remove(key)

   def get_free_space(self):
      value = []
      for y in self._items:
         value.append(y["value"])

      sum_ = self._capacity - sum(value)
      if sum_ > 0:
         return f"кол-во мест: {sum_}"
      elif sum_ < 0:
         return f"В магазин недостаточно места, попобуйте что то другое" 
   
   def get_items(self):
      print("в магазине хранится: ")
      for y in self._items:
         print(y["value"], y["item"])
      return ""
   
   def get_unique_items_count(self):
      number = []
      for y in self._items:
        number.append(y["item"])
      return len(set(number))
   
class Request:
   def __init__(self, user_str):
        data = self.get_data(user_str)
        self.from_ = data[4]
        self.to = data[6]
        self.amount = int(data[1])
        self.product = data[2]
   def get_data(self, user_str):
        return user_str.split(" ")
   
   def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'