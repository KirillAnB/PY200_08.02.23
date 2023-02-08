import random
import faker

TOOLS = 'items.txt'

with open(TOOLS, 'r', encoding='utf8') as file:
    data = file.readlines()


    def get_tool() -> str:
        result = random.choice(data).strip()
        return result


    def get_rating() -> int:
        rating = random.randint(1, 10)
        return rating


    def get_price() -> float:
        price = random.random() * random.randint(1000, 3000)
        return round(price, 2)

    def get_random_item():
        while True:
            random_tool = {
                'item_name' : get_tool(),
                'item_price': get_price(),
                'item_rating': get_rating()
            }
            yield random_tool

random_tool_generator = get_random_item()
random_tools_list = [next(random_tool_generator) for _ in range(5)]
print(random_tools_list)