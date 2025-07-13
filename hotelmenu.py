# Define the menulist of the restaurant
menu = {
    "Pizza" : 140,
    "Pasta" : 150,
    "Sandwich" : 70,
    "Burger" : 80,
    "Banana Shake" : 50
}

#print(menu)
#greet

print("Welcome to the Highway Restaurant")
print ("Below is the menu list :")
print("Pizza       : 140\nPasta       : 150\nSandwich    : 70\nBurger      :80\nBanana Shake: 50")

Order_total= 0
#140+70 =210

item_1 = input("Enter the name of the item you want to order: ")
#membership operator
if item_1 in menu:
    Order_total += menu[item_1]
    print(f"Your item {item_1} has been added to the order")

else: print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order == 'Yes':
    item_2 = input("Enter the name of the item you would like to add: ")
    if item_2 in menu:
        Order_total += menu[item_2]
        print(f"Your item {item_2} has been added to the order")
    else:
        print(f"Ordered item {item_2} is not available yet")



print(f"Total amount to pay is {Order_total}")



