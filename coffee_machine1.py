from coffee_menu import menu,resources

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





""" prompt user for what they would like to order"""
"""Prompt should repeat until system has turned off"""
machine= True
get_latte= resources["water"] - 200, resources['milk'] - 100 , resources["coffee"] - 24
get_cappuccino = resources["water"] - 250, resources['milk'] - 100, resources["coffee"]- 24
get_espresso = resources["water"] - 50, resources["coffee"]- 18

def make_order():
    

        
    if order == "latte":
        print("We've received your Latte order.")

        # For each order get cost from MENU dic and make sure enough money is put in slot or return money
        if resources["water"] < 200:
            print(f"Sorry, there's not enough water to complete order.")
        if resources["milk"] < 150:
            print(f"Sorry, there's not enough milk to complete order.")
        if resources["coffee"] < 24:
            print(f"Sorry, there's not enough coffee to complete order.")
        else:
            get_latte
            print(resources)
            

        # if resources["water"] < 200:
        #     print(f"Sorry, there's not enough water to complete order.")
        # if resources["milk"] < 150:
        #     print(f"Sorry, there's not enough milk to complete order.")
        # elif resources["coffee"] < 24:
        #     print(f"Sorry, there's not enough coffee to complete order.")

        
    
            

    elif order == 'Espresso':
        print("We've received your Espresso order")
    
        
        #For each order get cost from MENU dic and make sure enough money is put in slot or return money
        # if resources["water"] < 50:
        #     print(f"Sorry, there's not enough water to complete order.")
        # elif resources["coffee"] < 18:
        #     print(f"Sorry, there's not enough coffee to complete order.")

    elif order == 'Cappuccino':
        #For each order get cost from MENU dic and make sure enough money is put in slot or return money
        print("We've received your Cappuccino order")

        # if resources["water"] < 250:
        #     print(f"Sorry, there's not enough water to complete order.")
        # if resources["milk"] < 100:
        #     print(f"Sorry, there's not enough milk to complete order.")
        # elif resources["coffee"] < 24:
        #     print(f"Sorry, there's not enough coffee to complete order.")

while machine ==True:
    order=input("Hi, Would you like to order? (Espresso/ Latte/ Cappuccino) ")
    if order == "off":
        break
    elif order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
                    


make_order()

"""Print report that retunrns resource values"""
def insert_coin():
    
    print("PLEASE INSERT COINS:")
    quarters= int(input("How many quarters?"))
    dimes= int(input("How many dimes?"))
    nickles= int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
   
    quarters= quarters * 0.25
    dimes= dimes * 0.1
    nickles= nickles * 0.05
    pennies= pennies * 0.01
    # print(f"{dimes:.2f}")
    # print(quarters)
    # print(f"{nickles:.2f}")
    # print(round(pennies))
    total = quarters + dimes + nickles + pennies
    print(f"You have inserted ${total:.2f}")
    # print(resources)

    esp_price= menu["espresso"]['cost']
    cap_price= menu["cappuccino"]['cost']
    lat_price= menu["latte"]['cost']
    change = total - esp_price
    change1 = total - cap_price
    change2 = total - lat_price

    # if total >= esp_price:
    #     print(f"Here is your expresso!")
    #     if total > esp_price:
    #         print(f"Your change is {change:.2f}")
    if total >= cap_price:
        print(f"Here is your Latte!")
        if total > cap_price:
            print(f"Your change is {change1:.2f}")

    # if total >= lat_price:
    #     print(f"Here is your Latte!")
    #     if total > lat_price:
    #         print(f"Your change is {change2:.2f}")

    




    # print(lat_price)
    # print(esp_price)
    # print(cap_price)
    # print(total)
    # if total > 


insert_coin()

