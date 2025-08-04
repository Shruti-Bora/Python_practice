#Define the menu of cafe
menu = {
  "Pizza" : 100,
  "Pasta" : 50,
  "Burger" : 80,
  "Coffee" : 40,
  "Fries" : 50,
}

#Greet
print("Welcome to our Cafe")
#print("Pizza : Rs.100\nPasta : Rs.50\nBurger : Rs.80\nCoffee : Rs.40\nFries : Rs.50")
for item,price in menu.items():
  print(f"{item} :: Rs.{price}")

order_total = 0
ordered_items = [];

while True :
  item = input("Enter the item you want to order :: ")
  if item in menu:
    order_total += menu[item]
    ordered_items.append(item)
    print(f"Your item '{item}' has been added to your order!!")
  else:
    print(f"Sorry,{item} is not available in the menu!!")
  
  while True:
        another_item = input("Do you want to order something else? (Yes/No): ").strip().lower()
        if another_item == "yes":
            break  # Continue to order more items
        elif another_item == "no":
            break  # Exit the loop
        else:
            print("Please enter only 'Yes' or 'No'.")

  if another_item == "no":
    break  # Exit the main loop and show order summary

print("\n--- Order Summary ---")
if ordered_items:
    print("Items Ordered:", ', '.join(ordered_items))
    print(f"Total Bill: Rs.{order_total}")
else:
    print("No items were ordered.")     











# item_1 = input("Enter the name of the item you want to order :: ")
# if item_1 in menu:
#   order_total +=  menu[item_1]
#   print(f"Your item {item_1} has been added to your order!!")
# else:
#   print(f"Order item {item_1} is not available!!")


# another_item = input("Do you want something else to order?? (Yes/No)")
# if another_item == "Yes":
#   item_2 = input("Enter the second item you want to order :: ")
# if item_2 in menu:
#   order_total += menu[item_2]
#   print(f"Your item {item_2} has been added to your order!!")
# else:
#   print(f"Order item {item_1} is not available!!")

# print(f"The total amount of your order is :: {order_total}")
