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

def enough_resources(order_ingredients):
    """Return true if enough ingredients or False if not enough ingredients """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True

def process_coins():
    "Returns the toal calculated from coins inserted"
    print("PLEASE INSERT COINS:")
    total= int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money isn't enough"""

    if money_received >= drink_cost:
        change= round(money_received-drink_cost,2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

    
def make_coffee(drink_name, order_ingredients):
    """deduct the required ingreidents from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

machine= True

while machine ==True:
    order=input("Hi, What would you like to order? (Espresso/ Latte/ Cappuccino) ")
    if order == "off":
        break
    elif order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink= menu[order]
        if enough_resources(drink["ingredients"]):
            payment= process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
                    
