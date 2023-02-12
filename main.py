import hashlib
import random
import re
import item_generator


#Шаблоны для проверки пароля и логина
password_pattern = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$")
username_pattern = re.compile(r"^(?=.{4,12}$)(?![_.-])(?!.*[_.]{2})[a-zA-Z0-9._-]+(?<![_.])$")


class IDCounter:
    id = 0

    @classmethod
    def get_id(cls):
        return cls.id
    @staticmethod
    def increment_counter():
        IDCounter.id += 1

class Password:

    @staticmethod
    def valid_password(password):
        if password_pattern.fullmatch(password):
            return True
        else:
            raise ValueError('Bad password')
    @staticmethod
    def get_hash(password):
        if Password.valid_password(password):
            return hashlib.sha256(password.encode()).hexdigest()
    @staticmethod
    def check_hash(username, password):
        if isinstance(username, User) and username.password == Password.get_hash(password):
            print('Password accepted')
            return True
        else:
            print("Password is not accepted, try again")
            return False



class Product:
    def __init__(self, name, price, rating):
        IDCounter.increment_counter()
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


class Cart:
    def __init__(self):
        self.user_cart = []

    def put_to_cart(self,item):
        if isinstance(item, Product):
            self.user_cart.append(item)
    def del_from_cart(self, item):
        if item in self.user_cart:
            self.user_cart.remove(item)
        else:
            raise ValueError('В корзине нет такого товара')
    def show_cart(self):
        if len(self.user_cart) > 0:
            print("В корзине следующие товары:")
            for item in self.user_cart:
                print(item)
        else:
            print('Корзина пуста')
        return True
class User(Cart):

    def __init__(self, username, password):
        super().__init__()
        IDCounter.increment_counter()
        self.id = IDCounter.get_id()
        if self.valid_username(username):
            self.__username = username
        Password.valid_password(password)
        self.password = Password.get_hash(password)


    def valid_username(self,username):
        if username_pattern.fullmatch(username):
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
        return f'Пользователь с id {self.id}, имя {self.__username}, пароль "password1".'

    def __repr__(self):
        return f'{self.__class__.__name__}(username={self.__username!r}, password="password1")'
class Store():
    """Конструктор для строительного магазина"""


    def __init__(self, products):
        self.users_list = [] #Инициализируем список пользователей при создании магазина.
        self.products = products # Добавляем список продуктов, доступных в экземпляре магазина.

    def add_new_user(self, username, password):
        new_user = User(username, password)
        self.users_list.append(new_user)

    def show_shop_users(self):
        return f"Shop user {self.users_list}"
    def buy_item(self,username):
        item_to_buy = (random.choice(self.products))
        for user in self.users_list:
            if user.username == username:
                user.put_to_cart(item_to_buy)
                user.show_cart()
                return True
        else:
            raise ValueError(f'Покупатель с именем {username} не обнаружен.')





if __name__ == '__main__':
    user1 = User('Kirill', 'testPassword42')
    #проверка создания продуктов через генератор
    random_tool_generator = item_generator.get_random_item()
    random_tools_list = [next(random_tool_generator) for _ in range(20)]
    product_list = [Product(name=product_dict['item_name'], price=product_dict['item_price'],rating=product_dict['item_rating']) for product_dict in random_tools_list]
    # Проверка работы методов класса Password
    Password.check_hash(user1,'testPassword42')
    shop1 = Store(product_list)
    shop1.add_new_user('Kirill', 'testPassword42')
    shop1.add_new_user('Ivan', 'TestPassword42')
    shop1.buy_item('Ivan')

