import hashlib
import re
import item_generator
from sys import argv

#Для реализации с запуском через консоль
# user = argv[0]
# password = argv[1]

#Шаблоны для проверки пароля и логина
password_pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"
user_name_pattern = r"^(?=.{4,12}$)(?![_.-])(?!.*[_.]{2})[a-zA-Z0-9._-]+(?<![_.])$"


class IDCounter():
    id = 0
    def __init__(self):
        self.increment_counter()

    @classmethod
    def get_id(cls):
        return cls.id
    def increment_counter(self):
        IDCounter.id += 1

class Password():

    def __init__(self,password):
        IDCounter.increment_counter(self)
        self.id = IDCounter.get_id()
        self.password = password
        self.hash = Password.get_hash(self.password)
    def get_hash(password):
         return hashlib.sha256(password.encode()).hexdigest()
    def check_hash(self,password_to_check):
        hash_to_check = Password.get_hash(password_to_check)
        if self.hash == hash_to_check:
            return True
        else:
            return False



class Product():
    def __init__(self, name, price, rating):
        IDCounter.increment_counter(self)
        self.__id = IDCounter.get_id()
        self.__name = name
        if not isinstance(price, float):
            raise ValueError("Check price")
        self.set_price(price)
        if not isinstance(rating, int):
            raise TypeError
        self.rating = rating
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f'Товар #{self.__id} {self.__name} стоимостью {self.price} с рейтингом {self.rating}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, price={self.price!r}, rating={self.rating!r})'


class Cart():
    pass

class User():

    def __init__(self, username, password):
        IDCounter.increment_counter(self)
        self.id = IDCounter.get_id()
        self.__username = username
        self.password = Password.get_hash(password)
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        self.__username = username

    def __str__(self):
        return f'Пользователь с id {self.id}, имя {self.__username}, пароль {self.password}'

    def __repr__(self):
        return f'{self.__class__.__name__}(username={self.__username!r}, password=password1)'
class Store():
    """Конструктор для строительного магазина"""
    pass

if __name__ == '__main__':
    #создание и вывод просто для проверки
    item1 = Product('soap',100.0,10)
    print(good1.__str__())
    item2 = Product('soap2',150.0, 9)
    print(good2)
    user1 = User('Kirill','testpassword')
    print(user1.__str__())