menu= {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "cost": 3.0,
        },
        "cost": 3.0,
    }
}
profit= 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0
}

def resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry theres not enough {item}.")
            return False
        return True
        print(order_ingredients)
# print(menu["latte"]['cost'])
# print(resources["coffee"])
# print(resources['profit'])


# for menu["latte"] in menu:
#     if menu["latte"][0] > 200:
#         print("high")
    
    # if menu["latte"]['ingreidents']


