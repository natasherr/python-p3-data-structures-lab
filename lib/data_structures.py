spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    y = [x["name"] for x in spicy_foods]
    return y

def get_spiciest_foods(spicy_foods):
    y = [x for x in spicy_foods if x["heat_level"] > 5]
    return y

def print_spicy_foods(spicy_foods):
    for x in spicy_foods:
        print (f'{x["name"]} ({x["cuisine"]}) | Heat Level: {"🌶" * x["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for x in spicy_foods:
        if x["cuisine"] == cuisine:
            return x

def print_spiciest_foods(spicy_foods):
    for x in spicy_foods:
        if x["heat_level"] > 5:
            print (f'{x["name"]} ({x["cuisine"]}) | Heat Level: {"🌶" * x["heat_level"]}')

def get_average_heat_level(spicy_foods):
    x = sum([y["heat_level"] for y in spicy_foods])
    average = x / len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
