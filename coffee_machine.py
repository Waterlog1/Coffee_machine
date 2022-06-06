from coffee_menu import menu,resources





""" prompt user for what they would like to order"""
"""Prompt should repeat until system has turned off"""
machine= True


# def make_order():
#     while machine ==True:
#         order=input("Hi, Would you like to order? (Espresso/ Latte/ Cappuccino) ")
#         if order == "off":
#             break
#         elif order == 'report':
#             print (resources)
        
#         if order == "Latte":
#             print("Piece")
#             print("We've received your Latte order.")
#             #For each order get cost from MENU dic and make sure enough money is put in slot or return money
#             if resources["water"] < 200:
#                 print(f"Sorry, there's not enough water to complete order.")
#             if resources["milk"] < 150:
#                 print(f"Sorry, there's not enough milk to complete order.")
#             elif resources["coffee"] < 24:
#                 print(f"Sorry, there's not enough coffee to complete order.")
                

#         elif order == 'Espresso':
#             print("We've received your Espresso order")
#             print("scope")
            
#             #For each order get cost from MENU dic and make sure enough money is put in slot or return money
#             if resources["water"] < 50:
#                 print(f"Sorry, there's not enough water to complete order.")
#             elif resources["coffee"] < 18:
#                 print(f"Sorry, there's not enough coffee to complete order.")

#         elif order == 'Cappuccino':
#             #For each order get cost from MENU dic and make sure enough money is put in slot or return money
#             print("We've received your Cappuccino order")
#             print("snipe")

#             if resources["water"] < 250:
#                 print(f"Sorry, there's not enough water to complete order.")
#             if resources["milk"] < 100:
#                 print(f"Sorry, there's not enough milk to complete order.")
#             elif resources["coffee"] < 24:
#                 print(f"Sorry, there's not enough coffee to complete order.")
        
    


# make_order()

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

    




    print(lat_price)
    print(esp_price)
    print(cap_price)
    print(total)
    # if total > 


insert_coin()

