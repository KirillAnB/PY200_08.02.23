import hashlib
import re
import item_generator
from sys import argv

#Для реализации с запуском через консоль
# user = argv[0]
# password = argv[1]

#Шаблоны для проверки пароля и логина
password_pattern = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$")
username_pattern = re.compile(r"^(?=.{4,12}$)(?![_.-])(?!.*[_.]{2})[a-zA-Z0-9._-]+(?<![_.])$")


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
        self.check_password(password)
        self.hash = Password.get_hash(self.password)
    def check_password(self,password):
        if password_pattern.fullmatch(password):
            print('Good password')
            self.password = password
        else:
            raise ValueError('Bad password')
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
        if self.check_username(username):
            self.__username = username
        Password.check_password(self,password)
        self.password = Password.get_hash(password)

    def check_username(self,username):
        if username_pattern.fullmatch(username):
            print('Good username')
            return True
        else:
            raise ValueError("Bad username")


    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        self.__username = username

    def __str__(self):
        return f'Пользователь с id {self.id}, имя {self.__username}, пароль password1.'

    def __repr__(self):
        return f'{self.__class__.__name__}(username={self.__username!r}, password=password1)'
class Store():
    """Конструктор для строительного магазина"""
    pass

if __name__ == '__main__':
    #создание и вывод просто для проверки

    user1 = User('Kirill','tesT12345')
    print(user1.__str__())
    #проверка создания продуктов через генератор
    random_tool_generator = item_generator.get_random_item()
    random_tools_list = [next(random_tool_generator) for _ in range(5)]
    product_list = [Product(name=product_dict['item_name'], price=product_dict['item_price'],rating=product_dict['item_rating']) for product_dict in random_tools_list]
    for obj in product_list:
        print(obj)